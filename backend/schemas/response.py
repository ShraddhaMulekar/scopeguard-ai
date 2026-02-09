from pydantic import BaseModel
from typing import List, Optional, Dict

class Explanation(BaseModel):
    why_feasible: List[str]
    assumptions: List[str]
    monitoring: List[str]

class AnalysisResponse(BaseModel):
    risk_level: str
    risk_score: int
    summary: str
    key_issues: List[str]
    recommendations: List[str]
    explanation: Optional[Explanation] = None
    followup_questions: List[str] = []