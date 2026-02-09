from langchain_core.prompts import PromptTemplate

# High Risk Explanation Prompt

HIGH_RISK_EXPLANATION_PROMPT = PromptTemplate(
    input_variables=["idea", "analysis"],
    template="""
You are a senior software architect.

Based on the data below, return ONLY valid JSON.
Do NOT include explanations outside JSON.
Do NOT use markdown.
Do NOT add extra text.

Project: {idea}
Risk data: {analysis}

Return JSON in EXACTLY this format:

{
  "summary": "one paragraph explanation in simple words",
  "key_issues": [
    "issue 1",
    "issue 2",
    "issue 3"
  ],
  "recommendations": [
    "recommendation 1",
    "recommendation 2",
    "recommendation 3"
  ]
}
"""
)

# Low Risk Explanation Prompt
LOW_RISK_EXPLANATION_PROMPT = PromptTemplate(
    input_variables=[
        "idea",
        "total_risk"
    ],
    template="""
You are a senior software architect.

A deterministic system has classified the following project as LOW RISK.

Project Idea: {idea}
Total Risk Score: {total_risk}

Explain:
• Why the project is feasible
• What assumptions make it safe
• What should still be monitored

Respond in concise bullet points.
"""
)

# Follow-up Clarification Prompt 
# FOLLOWUP_CLARIFICATION_PROMPT = PromptTemplate(
#     input_variables=["missing_fields"],
#     template="""
# You are helping a user refine a project idea.

# The following information is missing:
# {missing_fields}

# Ask clear, short follow-up questions to collect this information.
# Do not analyze risk yet.
# """
# )

FOLLOWUP_CLARIFICATION_PROMPT = PromptTemplate(
    input_variables=["missing_fields"],
    template="""
You are helping refine a project proposal.

The following required fields are missing:
{missing_fields}

Return ONLY valid JSON in this format:

{
  "questions": [
    "Question 1",
    "Question 2"
  ]
}

Do not include explanations.
Do not include markdown.
"""
)