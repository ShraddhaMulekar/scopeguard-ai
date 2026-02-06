from typing import List
from llm.client import get_llm
from graph.risk_utils import calculate_risk, generate_recommendations, extract_json
from llm.prompts import (HIGH_RISK_EXPLANATION_PROMPT, LOW_RISK_EXPLANATION_PROMPT)
from llm.client import safe_invoke


llm = get_llm()

REQUIRED_FIELDS = ["experience", "time_weeks", "team", "tech"]

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


def followup_node(state):
    questions = []

    if "experience" in state["missing_fields"]:
        questions.append("What is your experience level? (beginner/intermediate/expert)")

    if "time_weeks" in state["missing_fields"]:
        questions.append("How many weeks do you have for this project?")

    if "team" in state["missing_fields"]:
        questions.append("How many people are in your team?")

    if "tech" in state["missing_fields"]:
        questions.append("What tech stack are you planning to use?")

    state["message"] = "I need a bit more info before analyzing:\n" + "\n".join(questions)
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
    state["recommendations"] = generate_recommendations(state)

    if total_risk >= 60:
        state["decision"] = "HIGH_RISK"
    else:
        state["decision"] = "LOW_RISK"

    return state

# High Risk Node

def high_risk_node(state: dict):
    print("⚙️ high risk node-6")
    structured_data = {
        "risk_level": "HIGH",
        "risk_score": state["total_risk"],
        "scope_risk": state["scope_risk"],
        "time_risk": state["time_risk"],
        "skill_risk": state["skill_risk"],
        "tech_risk": state["tech_risk"]
    }

    llm_response = safe_invoke(
        llm,
        HIGH_RISK_EXPLANATION_PROMPT.format(
            idea=state["idea"],
            analysis=structured_data
        )
    )

    parsed = extract_json(llm_response)

    state["final_analysis"] = {
        "risk_level": "HIGH",
        "risk_score": state["total_risk"],
        "summary": parsed["summary"],
        "key_issues": parsed["key_issues"],
        "recommendations": parsed["recommendations"]
    }

    state["decision"] = "FINAL"
    return state


# Low Risk Node
def low_risk_node(state):
    structured_response = {
        "risk_level": "LOW",
        "risk_score": state["total_risk"],
        "message": "Project looks feasible with current inputs",
        "recommendations": state["recommendations"]
    }

    prompt = LOW_RISK_EXPLANATION_PROMPT.format(
        idea=state["idea"],
        analysis=structured_response
    )

    state["final_analysis"] = {
        "data": structured_response,
        "explanation": safe_invoke(llm, prompt)
    }

    state["decision"] = "FINAL"
    # state.setdefault("recommendations", [])
    return state