import json

from analyzer.gemini_client import ask_gemini


def generate_resume_feedback(resume_text):

    prompt = f"""
You are an expert Resume Reviewer and ATS Expert.

Analyze the following resume.

Return ONLY valid JSON.

Do not explain.
Do not use markdown.

Format:

{{
    "resume_score": 0,
    "strengths": [],
    "weaknesses": [],
    "suggestions": []
}}

Rules:

- Resume score must be between 0 and 100.
- Strengths: 3 to 6 points.
- Weaknesses: 3 to 6 points.
- Suggestions: 3 to 6 professional recommendations.

Resume:

{resume_text}
"""

    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "").strip()

    try:
        return json.loads(response)

    except Exception:
        return {}