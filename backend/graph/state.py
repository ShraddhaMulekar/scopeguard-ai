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