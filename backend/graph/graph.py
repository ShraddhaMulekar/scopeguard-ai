from langgraph.graph import StateGraph, END
from graph.state import ProjectState
from graph.nodes import (
    scope_risk_node,
    time_risk_node,
    skill_risk_node,
    tech_risk_node,
    final_decision_node
)

def build_graph():
    graph = StateGraph(ProjectState)

    graph.add_node("scope", scope_risk_node)
    graph.add_node("time", time_risk_node)
    graph.add_node("skill", skill_risk_node)
    graph.add_node("tech", tech_risk_node)
    graph.add_node("final", final_decision_node)

    graph.set_entry_point("scope")

    graph.add_edge("scope", "time")
    graph.add_edge("time", "skill")
    graph.add_edge("skill", "tech")
    graph.add_edge("tech", "final")
    graph.add_edge("final", END)

    return graph.compile()