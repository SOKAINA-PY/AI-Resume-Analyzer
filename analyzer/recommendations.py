def generate_recommendations(
    score,
    matched_skills,
    missing_skills,
    resume_text
):
    recommendations = []

    # -------------------------
    # ATS Score
    # -------------------------

    if score < 60:
        recommendations.append(
            "Improve your resume to better match the job description."
        )

    elif score < 80:
        recommendations.append(
            "Your resume is good, but adding more relevant skills can improve your ATS score."
        )

    else:
        recommendations.append(
            "Excellent resume! Your profile matches the job description well."
        )

    # -------------------------
    # Missing Skills
    # -------------------------

    for skill in missing_skills:
        recommendations.append(
            f"Consider adding experience with {skill}."
        )

    # -------------------------
    # GitHub
    # -------------------------

    if "github" not in resume_text.lower():
        recommendations.append(
            "Include your GitHub profile to showcase your projects."
        )

    # -------------------------
    # LinkedIn
    # -------------------------

    if "linkedin" not in resume_text.lower():
        recommendations.append(
            "Add your LinkedIn profile."
        )

    # -------------------------
    # Resume Length
    # -------------------------

    if len(resume_text.split()) < 300:
        recommendations.append(
            "Add more details about your projects and work experience."
        )

    return recommendations