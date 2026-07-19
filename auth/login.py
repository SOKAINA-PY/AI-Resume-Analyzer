from database.supabase_client import supabase


def login_user(email, password):
    try:
        response = supabase.auth.sign_in_with_password(
            {
                "email": email,
                "password": password,
            }
        )

        return response

    except Exception as e:
        return str(e)