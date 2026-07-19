import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")

st.write("Welcome to AI Resume Analyzer")

if st.session_state.get("logged_in"):

    st.success(
        f"Welcome {st.session_state['user']}"
    )

else:

    st.warning(
        "Please login from the Login page."
    )