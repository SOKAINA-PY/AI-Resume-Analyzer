import json

from analyzer.gemini_client import ask_gemini


def match_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Compare the Resume with the Job Description.

Analyze the candidate professionally.

Return ONLY valid JSON.

Do NOT use markdown.
Do NOT explain.
Do NOT write anything outside JSON.

Format:

{{
    "ats_score": 0,
    "similarity_score": 0,
    "matched_skills": [],
    "missing_skills": [],
    "recommendations": []
}}

Rules:

- ATS score must be between 0 and 100.
- Similarity score must be between 0 and 100.
- matched_skills must contain only matching technical skills.
- missing_skills must contain only skills required by the Job Description but missing from the Resume.
- recommendations must contain 3 to 5 useful suggestions.

Resume:

{resume_text}

Job Description:

{job_description}
"""
    response = ask_gemini(prompt)

    response = response.replace("```json", "")
    response = response.replace("```", "").strip()

    try:
        return json.loads(response)

    except Exception:
        return {}