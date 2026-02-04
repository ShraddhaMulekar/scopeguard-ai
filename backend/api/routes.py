from fastapi import APIRouter, HTTPException
from schemas.request import ProjectRequest
from schemas.response import AnalysisResponse
from graph.workflow import risk_graph

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
def analyze_project(data: ProjectRequest):
    try:
        result = risk_graph.invoke({
            "idea": data.idea,
            "experience": data.experience,
            "time": data.time,
            "team": data.team,
            "tech": data.tech
        })

        return {
            "analysis": result["final_analysis"]
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
