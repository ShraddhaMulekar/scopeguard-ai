from fastapi import APIRouter, HTTPException
from schemas.request import ProjectRequest
from schemas.response import AnalysisResponse
from graph.workflow import run_risk_analysis

router = APIRouter()

@router.post("/analyze", response_model=AnalysisResponse)
def analyze_project(data: ProjectRequest):
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
        decision = result.get("decision")

        if decision == "ASK_FOLLOWUP":
            # Return only followup questions for missing info
            return AnalysisResponse(
                risk_level="UNKNOWN",
                risk_score=0,
                summary="",
                key_issues=[],
                recommendations=[],
                explanation=None,
                followup_questions=result.get("message", [])
            )

        # ✅ FINAL ANALYSIS
        final = result["final_analysis"]

        # Explanation is already structured (why_feasible, assumptions, monitoring)
        explanation_obj = final.get("explanation", None)

        return AnalysisResponse(
            risk_level=final["risk_level"],
            risk_score=final["risk_score"],
            summary=final.get("summary", ""),
            key_issues=final.get("key_issues", []),
            recommendations=final.get("recommendations", []),
            explanation=explanation_obj,
            followup_questions=[]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"ScopeGuard AI failed: {str(e)}"
        )