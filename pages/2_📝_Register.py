import streamlit as st

from auth.register import register_user

st.set_page_config(
    page_title="Register",
    page_icon="📝"
)

st.title("📝 Create Account")

st.write("Create your AI Resume Analyzer account")

email = st.text_input("Email")

password = st.text_input(
    "Password",
    type="password"
)

if st.button("Register"):

    if email == "" or password == "":

        st.warning("Please fill all fields.")

    else:

        response = register_user(
            email,
            password
        )

        if isinstance(response, str):

            st.error(response)

        else:

            st.success("Account created successfully!")

            st.info("You can now Login.")