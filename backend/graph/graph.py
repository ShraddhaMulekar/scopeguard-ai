from langgraph.graph import StateGraph, END
from graph.state import ProjectState
from graph.nodes import (
    detect_missing_info,
    followup_node,
    risk_analysis_node,
    high_risk_node,
    low_risk_node
)

def route_by_risk(state):
    print("total_risk",state["total_risk"])
    if state["total_risk"] >= 60:
        return "HIGH"
    return "LOW"


def build_graph():
    print("🧩 Building graph-5")
    graph = StateGraph(ProjectState)

    # Nodes
    graph.add_node("detect_missing", detect_missing_info)
    graph.add_node("followup", followup_node)
    graph.add_node("risk_analysis", risk_analysis_node)
    graph.add_node("high_risk", high_risk_node )
    graph.add_node("low_risk", low_risk_node )

    # Entry point
    graph.set_entry_point("detect_missing")

    # If info missing → ask follow-up
    # Else → analyze risk
    graph.add_conditional_edges(
        "detect_missing",
        lambda state: state["decision"],
        {
            "ASK_FOLLOWUP": "followup",
            "ANALYZE_RISK": "risk_analysis"
        }
    )

     # Risk routing
    graph.add_conditional_edges(
        "risk_analysis",
        route_by_risk,
        {
            "HIGH": "high_risk",
            "LOW": "low_risk"
        }
    )

    # End nodes
    graph.add_edge("followup", END)
    graph.add_edge("high_risk", END)
    graph.add_edge("low_risk", END)

    return graph.compile()