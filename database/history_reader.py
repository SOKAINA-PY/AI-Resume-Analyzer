from database.supabase_client import supabase


def get_history(user_email):

    response = (
        supabase
        .table("analysis_history")
        .select("*")
        .eq("user_email", user_email)
        .order("created_at", desc=True)
        .execute()
    )

    return response.data