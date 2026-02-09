from graph.graph import build_graph
from graph.state import ProjectState

# Build the compiled LangGraph once
risk_graph = build_graph()


def run_risk_analysis(input_state):
    # Normalize / default state
    state = {
        "idea": input_state.get("idea", ""),
        "experience": input_state.get("experience"),
        "time_weeks": input_state.get("time_weeks"),
        "team": input_state.get("team"),
        "tech": input_state.get("tech"),
        # Graph-controlled fields
        "missing_fields": [],
        "decision": None,
        "message": None,
        "final_analysis": None,
        "recommendations": [],
            # Risk scores (IMPORTANT)
        "scope_risk": 0,
        "time_risk": 0,
        "skill_risk": 0,
        "tech_risk": 0,
        "total_risk": 0,
    }
    result = risk_graph.invoke(state)
    return result