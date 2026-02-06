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
    print("\n🚀 API HIT /analyze")
    print("📥 Incoming request1:", data)

    # ✅ Build initial state correctly
    input_state = {
        "idea": data.idea,
        "experience": data.experience,
        "time_weeks": data.time_weeks,  
        "team": data.team,
        "tech": data.tech
    }
    print('input_state-routes1',input_state)
    try:
        # Run LangGraph workflow
        result = run_risk_analysis(input_state)
        print(result, 'result27-routes1')
        # 🔁 FOLLOW-UP REQUIRED
        if result.get("decision") == "ASK_FOLLOWUP":
            return AnalysisResponse(
                risk_level=result["final_analysis"]["risk_level"],
                risk_score=result["final_analysis"]["risk_score"],
                summary=result["final_analysis"]["summary"],
                key_issues=result["final_analysis"]["key_issues"],
                recommendations=result["final_analysis"]["recommendations"],
                followup_questions=result("message", [])
            )

        # ✅ FINAL ANALYSIS
        final = result["final_analysis"]
        return AnalysisResponse(
                # risk_level=result["final_analysis"]["risk_level"],
                # risk_score=result["final_analysis"]["risk_score"],
                # summary=result["final_analysis"]["summary"],
                # key_issues=result["final_analysis"]["key_issues"],
                # recommendations=result["final_analysis"]["recommendations"],
                # followup_questions=[]
                risk_level=final["risk_level"],
                risk_score=final["risk_score"],
                summary=final["summary"],
                key_issues=final["key_issues"],
                recommendations=final["recommendations"],
                followup_questions=[]
        )

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"ScopeGuard AI failed: {str(e)}"
        )