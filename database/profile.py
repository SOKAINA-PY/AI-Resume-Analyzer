from database.supabase_client import supabase


def get_profile(email):

    response = (
        supabase
        .table("profiles")
        .select("*")
        .eq("email", email)
        .execute()
    )

    if response.data:
        return response.data[0]

    return None