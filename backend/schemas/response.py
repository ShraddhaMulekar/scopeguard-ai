from typing import List, Optional
from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    risk_level: Optional[str]
    risk_score: Optional[int]
    summary: Optional[str]
    key_issues: List[str] = []
    recommendations: List[str] = []
    followup_questions: List[str] = []