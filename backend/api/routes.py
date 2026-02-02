from fastapi import APIRouter, HTTPException
from schemas.request import ProjectRequest
from schemas.response import AnalysisResponse
from llm.client import get_llm
from llm.prompts import PROJECT_ANALYSIS_PROMPT

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
def analyze_project(data:ProjectRequest):
    try:
        llm=get_llm()
        prompt=PROJECT_ANALYSIS_PROMPT.format(
            idea=data.idea,
            experience=data.experience,
            time=data.time,
            team=data.team,
            tech=data.tech
        )
        result=llm.invoke(prompt)
        return {"analysis": result.content}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))