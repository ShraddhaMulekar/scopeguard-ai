from pydantic import BaseModel
from typing import List, TypedDict

class AnalysisResponse(TypedDict):
    risk_level: str
    risk_score: int
    summary: str
    key_issues: List[str]
    recommendations: List[str]
