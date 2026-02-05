"""
Deterministic risk engine for ScopeGuard AI
No LLM calls allowed in this file
Pure logic + predictable output
"""

def calculate_risk(time_weeks, team_size, experience, tech):
    """
    Returns:
    scope_risk, time_risk, skill_risk, tech_risk, total_risk
    """

    # Normalize inputs
    experience = experience.lower()
    tech = tech.lower()

    # Scope vs Time Risk
    if time_weeks <= 2:
        scope_risk = 30
        time_risk = 30
    elif time_weeks <= 4:
        scope_risk = 20
        time_risk = 20
    elif time_weeks <= 8:
        scope_risk = 10
        time_risk = 10
    else:
        scope_risk = 5
        time_risk = 5

    # Skill Risk
    if experience == "beginner":
        skill_risk = 30
    elif experience == "intermediate":
        skill_risk = 15
    else:
        skill_risk = 5

    # Tech Risk (keyword-based)
    high_risk_tech_keywords = [
        "llm", "ai", "ml", "blockchain", "crypto", "web3"
    ]

    uses_high_risk_tech = any(
        keyword in tech for keyword in high_risk_tech_keywords
    )

    if uses_high_risk_tech and experience == "beginner":
        tech_risk = 25
    elif uses_high_risk_tech:
        tech_risk = 15
    else:
        tech_risk = 5

    # Team Size Modifier
    if team_size == 1:
        team_modifier = 15
    elif team_size <= 3:
        team_modifier = 10
    else:
        team_modifier = 0

    # Final Risk Score
    total_risk = (
        scope_risk +
        time_risk +
        skill_risk +
        tech_risk +
        team_modifier
    )

    total_risk = min(total_risk, 100)

    return (
        scope_risk,
        time_risk,
        skill_risk,
        tech_risk,
        total_risk
    )