from database.supabase_client import supabase


def register_user(email, password):

    try:

        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
            }
        )

        if response.user:

            supabase.table("profiles").insert(
                {
                    "email": email,
                    "full_name": ""
                }
            ).execute()

        return response

    except Exception as e:
        return str(e)