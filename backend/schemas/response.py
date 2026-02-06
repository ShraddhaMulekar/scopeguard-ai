from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class AnalysisResponse(BaseModel):
        # risk_level: str
        # risk_score: int
        # summary: Optional[str]
        # key_issues: List[str]
        # recommendations: List[str]
        # followup_questions: List[str] = []
        risk_level: Optional[str] = None
        risk_score: Optional[int] = None
        summary: Optional[str] = None
        key_issues: List[str] = []
        recommendations: List[dict] = []
        followup_questions: List[str] = []
