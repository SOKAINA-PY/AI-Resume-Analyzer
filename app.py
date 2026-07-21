import streamlit as st

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="🤖",
    layout="wide"
)

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

st.title("🤖 AI Resume Analyzer")

st.markdown("""
### Smart AI-powered Resume Analysis

Upload your resume, compare it with a job description, improve your ATS score, and get AI-powered recommendations.
""")

st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("🤖 AI", "Gemini")

with col2:
    st.metric("📄 Resume", "PDF")

with col3:
    st.metric("📊 ATS", "Analyzer")

st.divider()

st.subheader("✨ Features")

c1, c2 = st.columns(2)

with c1:
    st.success("📄 Resume Analyzer")
    st.success("🤖 AI Resume Review")
    st.success("📊 ATS Matching")

with c2:
    st.success("📜 Analysis History")
    st.success("👤 User Profile")
    st.success("💌 Cover Letter (Coming Soon)")

st.divider()

if st.session_state.logged_in:
    st.success(f"👋 Welcome {st.session_state['user']}")
else:
    st.warning("🔐 Please login to access all features.")