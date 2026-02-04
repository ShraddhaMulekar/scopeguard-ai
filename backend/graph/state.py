from typing import TypedDict, Optional, List

class ScopeState(TypedDict):
    project_description: str
    timeline_weeks: Optional[int]
    team_size: Optional[int]
    experience_level: Optional[str]

    missing_fields: List[str]
    risk_score: Optional[int]
    decision: Optional[str]
    message: Optional[str]