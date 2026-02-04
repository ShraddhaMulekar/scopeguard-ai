from langchain_groq import ChatGroq
from app.config import GROQ_API_KEY, MODEL_NAME


def get_llm():
    """
    Returns Groq LLM client.
    This function ONLY creates the client.
    """
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing")

    return ChatGroq(
        api_key=GROQ_API_KEY,
        model=MODEL_NAME,
        temperature=0.2,
        timeout=10
    )


def safe_invoke(llm, prompt: str) -> str:
    """
    Safely invoke LLM.
    If Groq fails, return a friendly fallback message.
    """
    try:
        response = llm.invoke(prompt)
        return response.content
    except Exception as e:
        return (
            "⚠️ AI service is temporarily unavailable.\n"
            "Based on deterministic analysis, the risk assessment "
            "has been completed, but detailed explanation is limited."
        )