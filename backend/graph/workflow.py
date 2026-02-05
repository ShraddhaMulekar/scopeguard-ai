from graph.graph import build_graph
from graph.state import ProjectState

# Build the compiled LangGraph once
risk_graph = build_graph()


def run_risk_analysis(input_state: ProjectState):
    """
    Entry point to run ScopeGuard risk analysis
    Ensures state is always complete
    """

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
        "final_analysis": None
    }

    # Invoke LangGraph safely
    result = risk_graph.invoke(state)
    print("run risk", result)
    return result


if __name__ == "__main__":
    test_input = {
        "idea": "AI Resume Analyzer",
        "team": 1
    }

    output = run_risk_analysis(test_input)
    print(output)