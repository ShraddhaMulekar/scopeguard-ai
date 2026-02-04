from typing import List
from llm.client import get_llm
from graph.risk_utils import calculate_risk

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
    scope_risk, time_risk, skill_risk, tech_risk, total = calculate_risk(
        time_weeks=state["time_weeks"],
        team_size=state["team"],
        experience=state["experience"],
        tech=state["tech"]
    )

    state["scope_risk"] = scope_risk
    state["time_risk"] = time_risk
    state["skill_risk"] = skill_risk
    state["tech_risk"] = tech_risk
    state["total_risk"] = total

    if total >= 60:
        state["decision"] = "HIGH_RISK"
    else:
        state["decision"] = "LOW_RISK"

    return state