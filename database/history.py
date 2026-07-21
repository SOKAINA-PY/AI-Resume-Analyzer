from database.supabase_client import supabase


def save_analysis(user_email, result):

    data = {
        "user_email": user_email,
        "ats_score": result["ats_score"],
        "similarity_score": result["similarity_score"],
        "matched_skills": result["matched_skills"],
        "missing_skills": result["missing_skills"],
        "recommendations": result["recommendations"],
    }

    supabase.table("analysis_history").insert(data).execute()