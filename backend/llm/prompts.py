from langchain.prompts import PromptTemplate

PROJECT_ANALYSIS_PROMPT = PromptTemplate(
    input_variables=[
        "idea",
        "experience",
        "time",
        "team",
        "tech"
    ],
    template='''
You are an expert Software Project reviewer.

Analyze the following project idea and identify potential risks.

Project Idea: {idea}
Experience Level: {experience}
Time Available: {time}
Team Size: {team}
Tech Stack: {tech}

Give:
1. Main risks
2. Scope issues
3. Timeline realism
4. Skill mismatch (if any)

Respond in clear bullet points.
'''
)