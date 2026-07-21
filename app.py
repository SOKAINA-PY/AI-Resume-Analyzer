import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 AI Resume Analyzer")

st.markdown("""
# Welcome 👋

Analyze your Resume with AI.

### Features

- 📄 Resume Analyzer
- 🤖 AI Resume Review
- 📊 ATS Matching
- 📜 Analysis History
- 👤 User Profile
""")

st.divider()

if st.session_state.get("logged_in"):
    st.success(f"Welcome {st.session_state['user']} 🎉")
else:
    st.info("Please login from the Login page.")