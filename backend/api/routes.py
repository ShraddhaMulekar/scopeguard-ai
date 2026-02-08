from fastapi import APIRouter, HTTPException
from schemas.request import ProjectRequest
from schemas.response import AnalysisResponse
from graph.workflow import run_risk_analysis

router = APIRouter()

@router.post("/analyze")
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
    # print('data',data)
    print('input_state-routes1',input_state)
    try:
        # Run LangGraph workflow
        result = run_risk_analysis(input_state)
        print("RESULT TYPE:", type(result))
        print("RESULT KEYS:", result.keys())
        print("DECISION:", result.get("decision"))
        print("FINAL_ANALYSIS:", result.get("final_analysis"))

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


# from fastapi import APIRouter, HTTPException
# from schemas.request import ProjectRequest
# from graph.workflow import run_risk_analysis

# router = APIRouter()

# @router.post("/analyze")
# def analyze_project(data: ProjectRequest):
#     print("\n🚀 API HIT /analyze")
#     print("📥 Incoming request:", data)

#     input_state = {
#         "idea": data.idea,
#         "experience": data.experience,
#         "time_weeks": data.time_weeks,
#         "team": data.team,
#         "tech": data.tech
#     }

#     print("🧩 input_state:", input_state)

#     try:
#         result = run_risk_analysis(input_state)

#         print("\n🧠 RAW RESULT FROM GRAPH")
#         print("TYPE:", type(result))
#         print("KEYS:", result.keys())
#         print("FULL RESULT:\n", result)

#         # ✅ SAFE ACCESS
#         final = result.get("final_analysis")

#         if final is None:
#             raise ValueError("final_analysis is None")

#         return {
#             "decision": result.get("decision"),
#             "final_analysis": final
#         }

#     except Exception as e:
#         print("❌ ERROR:", str(e))
#         raise HTTPException(
#             status_code=500,
#             detail=f"ScopeGuard AI failed: {str(e)}"
#         )
