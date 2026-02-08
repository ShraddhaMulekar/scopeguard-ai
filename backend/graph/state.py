# from typing import TypedDict, Optional, List

# class ProjectState(TypedDict):
#     # ===== User Inputs =====
#     idea: str
#     experience: Optional[str]        # beginner / intermediate / expert
#     time_weeks: Optional[int]        # numeric for scoring
#     team: Optional[int]
#     tech: Optional[str]

#     # ===== Internal Agent Logic =====
#     missing_fields: List[str]         # for follow-up questions
#     decision: Optional[str]           # ASK_FOLLOWUP / ANALYZE / HIGH_RISK / LOW_RISK

#     # ===== Risk Analysis =====
#     scope_risk: Optional[int]
#     time_risk: Optional[int]
#     skill_risk: Optional[int]
#     tech_risk: Optional[int]
#     total_risk: Optional[int]

#     # ===== Output =====
#     final_analysis: Optional[str]
#     message: Optional[str]            # user-facing response
#     recommendations: Optional[dict]
#     summary: Optional[str]

#     print("🧾 Mapping final state response-4")


from typing import TypedDict, Optional, List, Dict, Any

class AnalysisDict(TypedDict):
    summary: str
    key_issues: List[str]
    recommendations: List[str]

class ProjectState(TypedDict):
    # inputs
    idea: str
    experience: Optional[str]
    time_weeks: Optional[int]
    team: Optional[int]
    tech: Optional[str]

    # control
    missing_fields: List[str]
    decision: Optional[str]

    # risk
    scope_risk: int
    time_risk: int
    skill_risk: int
    tech_risk: int
    total_risk: int

    # output
    final_analysis: Optional[AnalysisDict]
    message: Optional[str]
