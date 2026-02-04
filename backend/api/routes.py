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

    # Build initial state from request
    input_state = {
        "idea": data.idea,
        "experience": data.experience,
        "time_weeks": data.time,  # renamed for consistency with state.py
        "team": data.team,
        "tech": data.tech
    }

    try:
        # Run the full LangGraph workflow
        result = run_risk_analysis(input_state)

        # Handle follow-up scenario
        if result.get("decision") == "ASK_FOLLOWUP":
            return {
                "analysis": None,
                "followup_questions": result.get("message", [])
            }

        # Handle final analysis scenario
        return {
            "analysis": result.get("final_analysis"),
            "followup_questions": []
        }

    except Exception as e:
        # Safe fallback
        raise HTTPException(
            status_code=500,
            detail=f"ScopeGuard AI failed: {str(e)}"
        )