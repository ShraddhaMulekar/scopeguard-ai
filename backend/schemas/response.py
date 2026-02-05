from typing import List, Optional
from pydantic import BaseModel

class AnalysisResponse(BaseModel):
    analysis: Optional[str] = None
    followup_questions: List[str] = []