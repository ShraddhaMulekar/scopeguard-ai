from fastapi import APIRouter, HTTPException
from schemas.request import ProjectRequest
from schemas.response import AnalysisResponse
from graph.workflow import run_risk_analysis

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
def analyze_project(data: ProjectRequest):
    """
    Analyze a project idea using ScopeGuard AI.
    Handles missing info, high/low risk, and safe LLM calls.
    """

    # ✅ Build initial state correctly
    input_state = {
        "idea": data.idea,
        "experience": data.experience,
        "time_weeks": data.time_weeks,  
        "team": data.team,
        "tech": data.tech
    }

    try:
        # Run LangGraph workflow
        result = run_risk_analysis(input_state)

        # 🔁 FOLLOW-UP REQUIRED
        if result.get("decision") == "ASK_FOLLOWUP":
            return AnalysisResponse(
                analysis=None,
                followup_questions=result.get("message", [])
            )

        # ✅ FINAL ANALYSIS
        return AnalysisResponse(
            analysis=result.get("final_analysis", ""),
            followup_questions=[]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"ScopeGuard AI failed: {str(e)}"
        )