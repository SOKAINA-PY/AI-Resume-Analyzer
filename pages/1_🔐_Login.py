import streamlit as st
from auth.login import login_user

st.set_page_config(
    page_title="Login",
    page_icon="🔐"
)

st.title("🔐 Login")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Login"):

    if email == "" or password == "":
        st.warning("Please fill all fields.")

    else:

        response = login_user(email, password)

        if isinstance(response, str):

            st.error(response)

        else:

            st.success("Login Successful 🎉")

            st.session_state["logged_in"] = True
            st.session_state["user"] = response.user.email