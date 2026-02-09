from typing import List
from llm.client import get_llm
from graph.risk_utils import calculate_risk, generate_recommendations, extract_json
from llm.prompts import (HIGH_RISK_EXPLANATION_PROMPT, LOW_RISK_EXPLANATION_PROMPT, FOLLOWUP_CLARIFICATION_PROMPT)
from llm.client import safe_invoke
from schemas.schema import HighRiskLLMResponse
import json
from graph.state import ProjectState


llm = get_llm()

REQUIRED_FIELDS = ["experience", "time_weeks", "team", "tech"]

import json
import re

def extract_json_safe(text: str) -> dict:
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON object found in LLM output")
    return json.loads(match.group())


def detect_missing_info(state):
    missing = []

    for field in REQUIRED_FIELDS:
        if not state.get(field):
            missing.append(field)

    state["missing_fields"] = missing

    if missing:
        state["decision"] = "ASK_FOLLOWUP"
    else:
        state["decision"] = "ANALYZE_RISK"

    return state

# follow up Node
def followup_clarification_node(state: ProjectState) -> ProjectState:
    missing = state.get("missing_fields", [])

    if not missing:
        return state  # nothing to ask

    prompt = FOLLOWUP_CLARIFICATION_PROMPT.format(
        missing_fields=", ".join(missing)
    )

    raw = safe_invoke(llm, prompt)
    parsed = extract_json_safe(raw)

    state["decision"] = "ASK_FOLLOWUP"
    state["message"] = parsed.get("questions", [])

    return state


def risk_analysis_node(state):
    scope_risk, time_risk, skill_risk, tech_risk, total_risk = calculate_risk(
        time_weeks=state["time_weeks"],
        team_size=state["team"],
        experience=state["experience"],
        tech=state["tech"]
    )

    state["scope_risk"] = scope_risk
    state["time_risk"] = time_risk
    state["skill_risk"] = skill_risk
    state["tech_risk"] = tech_risk
    state["total_risk"] = total_risk

    # ✅ ADD THIS LINE (THIS FIXES YOUR ERROR)
    state["recommendations"] = [
        rec["message"] for rec in generate_recommendations(state)
    ]

    if total_risk >= 60:
        state["decision"] = "HIGH_RISK"
    else:
        state["decision"] = "LOW_RISK"

    return state

# High Risk Node
def high_risk_node(state: ProjectState) -> ProjectState:
    # --- Build prompt manually ---
    prompt_text = f"""
You are a senior software architect.

Based on the data below, return ONLY valid JSON.
Do NOT include explanations outside JSON.
Do NOT use markdown.
Do NOT add extra text.

Project: {state['idea']}
Risk data:
  scope_risk: {state['scope_risk']}
  time_risk: {state['time_risk']}
  skill_risk: {state['skill_risk']}
  tech_risk: {state['tech_risk']}
  total_risk: {state['total_risk']}

Return JSON in EXACTLY this format:

{{
  "summary": "one paragraph explanation in simple words",
  "key_issues": [
    "issue 1",
    "issue 2",
    "issue 3"
  ],
  "recommendations": [
    "recommendation 1",
    "recommendation 2",
    "recommendation 3"
  ]
}}
"""
    # print("🟡 BEFORE LLM CALL")

    # --- Call LLM safely ---
    try:
        raw = safe_invoke(llm, prompt_text)
    except Exception as e:
        print("❌ AI call failed:", e)
        raw = """{
            "summary": "High risk detected, but AI explanation unavailable.",
            "key_issues": ["Risk assessment completed"],
            "recommendations": ["Review project manually"]
        }"""

    # print("🟢 AFTER LLM CALL")
    # print("🧠 RAW LLM OUTPUT:\n", raw)

    # --- Parse AI response safely ---
    parsed = extract_json_safe(raw)
    summary = parsed.get(
        "summary", "This project is considered high risk based on multiple constraints."
    )
    key_issues = parsed.get("key_issues", [])
    recommendations = parsed.get("recommendations", [])

    # --- Update state ---
    state["final_analysis"] = {
        "risk_level": "HIGH",
        "risk_score": state["total_risk"],
        "summary": summary,
        "key_issues": key_issues,
        "recommendations": recommendations
    }

    state["decision"] = "FINAL"
    return state

# Low Risk Node
def low_risk_node(state:ProjectState) ->ProjectState:
    # Base analysis
    state["final_analysis"] = {
        "risk_level": "LOW",
        "risk_score": state["total_risk"],
        "summary": "This project is feasible with current inputs.",
        "key_issues": [],
        "recommendations": state.get("recommendations", [])
    }

    # Prompt for LLM (plain text)
    prompt_text = f"""
You are a senior software architect.

A deterministic system has classified the following project as LOW RISK.

Project Idea: {state['idea']}
Total Risk Score: {state['total_risk']}

Provide structured explanation in JSON format with keys:
- "why_feasible" : list of strings
- "assumptions" : list of strings
- "monitoring" : list of strings
Do NOT include markdown, just plain text.
"""

    # Call LLM safely
    raw_response = safe_invoke(llm, prompt_text)

    # Parse AI output as JSON safely
    try:
        explanation_structured = extract_json_safe(raw_response)
    except Exception:
        # fallback if AI fails
        explanation_structured = {
            "why_feasible": ["The project is considered low risk based on available data."],
            "assumptions": [],
            "monitoring": []
        }

    # Store structured explanation
    state["final_analysis"]["explanation"] = explanation_structured
    state["decision"] = "FINAL"

    return state