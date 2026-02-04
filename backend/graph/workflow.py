from graph.graph import build_graph
from graph.state import ProjectState

# Build the compiled LangGraph once
risk_graph = build_graph()

def run_risk_analysis(input_state: ProjectState):
    """
    Entry point to run ScopeGuard risk analysis
    """
    result = risk_graph.invoke(input_state)
    return result


if __name__ == "__main__":
    test_input = {
        "idea": "AI Resume Analyzer",
        "team": 1
    }

    output = run_risk_analysis(test_input)
    print(output)