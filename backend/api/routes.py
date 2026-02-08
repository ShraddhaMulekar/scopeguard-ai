from fastapi import APIRouter, HTTPException
from schemas.request import ProjectRequest
from schemas.response import AnalysisResponse
from graph.workflow import run_risk_analysis

router = APIRouter()

@router.post("/analyze")
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
            return {
                "decision": "ASK_FOLLOWUP",
                "questions": result.get("message", [])
            }

        return {
            "decision": "FINAL",
            "final_analysis": result["final_analysis"]
        }
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
