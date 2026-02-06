from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class AnalysisResponse(BaseModel):
        risk_level: str
        risk_score: int
        summary: str
        key_issues: List[str]
        recommendations: List[str]
        followup_questions: List[str] = []
