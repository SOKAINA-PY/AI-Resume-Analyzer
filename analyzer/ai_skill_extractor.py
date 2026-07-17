import json

from analyzer.gemini_client import ask_gemini


def extract_skills_ai(resume_text):

    prompt = f"""
You are an expert ATS Resume Analyzer.

Analyze the following resume carefully.

Extract ONLY real skills explicitly mentioned in the resume.

Rules:

- Return ONLY valid JSON.
- No explanations.
- No markdown.
- No comments.
- Do not invent skills.
- Ignore education.
- Ignore universities.
- Ignore job titles.
- Ignore project names.
- Ignore company names.
- Ignore certifications.
- Ignore sentences.
- Ignore responsibilities.

Categorize the skills into:

{{
  "Programming Languages": [],
  "Frameworks": [],
  "Libraries": [],
  "AI & Machine Learning": [],
  "Databases": [],
  "Cloud & DevOps": [],
  "Embedded Systems": [],
  "Networking": [],
  "CAD Software": [],
  "Simulation Software": [],
  "Office Tools": [],
  "Design Tools": [],
  "Soft Skills": [],
  "Languages": []
}}

Resume:

{resume_text}
"""

    response = ask_gemini(prompt)

    print("\n========== GEMINI RESPONSE ==========\n")
    print(response)
    print("\n=====================================\n")

    response = response.replace("```json", "")
    response = response.replace("```", "").strip()

    try:
        return json.loads(response)

    except Exception as e:

        print("JSON Error:", e)

        return {}