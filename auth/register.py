from database.supabase_client import supabase


def register_user(email, password):
    try:
        response = supabase.auth.sign_up(
            {
                "email": email,
                "password": password,
            }
        )

        return response

    except Exception as e:
        return str(e)