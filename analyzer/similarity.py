from difflib import SequenceMatcher


def calculate_similarity(resume_text, job_description):
    """
    Calculate text similarity between Resume and Job Description.
    Returns a percentage between 0 and 100.
    """

    similarity = SequenceMatcher(
        None,
        resume_text.lower(),
        job_description.lower()
    ).ratio()

    return int(similarity * 100)