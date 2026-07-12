def calculate_ats_score(resume_skills, job_description, skills_database):
    """
    Compare resume skills with skills found in the job description.
    Returns:
        score,
        matched_skills,
        missing_skills
    """

    job_description = job_description.lower()

    required_skills = []

    # Find required skills in the Job Description
    for category, skills in skills_database.items():

        for skill in skills:

            if skill.lower() in job_description:
                required_skills.append(skill)

    required_skills = list(set(required_skills))

    matched_skills = []

    for skill in resume_skills:

        if skill in required_skills:
            matched_skills.append(skill)

    missing_skills = []

    for skill in required_skills:

        if skill not in matched_skills:
            missing_skills.append(skill)

    # Calculate score
    if len(required_skills) == 0:
        score = 0
    else:
        score = int(
            (len(matched_skills) / len(required_skills)) * 100
        )

    return score, matched_skills, missing_skills
