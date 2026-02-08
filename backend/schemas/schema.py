from typing import TypedDict, List

class HighRiskLLMResponse(TypedDict):
    summary: str
    key_issues: List[str]
    recommendations: List[str]
