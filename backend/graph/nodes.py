from llm.client import get_llm

llm = get_llm()  

def scope_risk_node(state):
    response = llm.invoke(f"""
    Analyze project scope risk.
    Project idea: {state['idea']}
    Experience: {state['experience']}
    Time: {state['time']}
    """)
    state["scope_risk"] = response.content
    return state


def time_risk_node(state):
    response = llm.invoke(f"""
    Analyze time risk.
    Time available: {state['time']}
    Project idea: {state['idea']}
    """)
    state["time_risk"] = response.content
    return state


def skill_risk_node(state):
    response = llm.invoke(f"""
    Analyze skill risk.
    Experience level: {state['experience']}
    Tech stack: {state['tech']}
    """)
    state["skill_risk"] = response.content
    return state


def tech_risk_node(state):
    response = llm.invoke(f"""
    Analyze technology risk.
    Tech stack: {state['tech']}
    Team size: {state['team']}
    """)
    state["tech_risk"] = response.content
    return state


def final_decision_node(state):
    response = llm.invoke(f"""
    Based on the following risks, predict project failure probability
    and give a clear recommendation.

    Scope Risk: {state['scope_risk']}
    Time Risk: {state['time_risk']}
    Skill Risk: {state['skill_risk']}
    Tech Risk: {state['tech_risk']}
    """)
    state["final_analysis"] = response.content
    return state