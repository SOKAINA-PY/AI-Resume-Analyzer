import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# Title
st.title("📄 AI Resume Analyzer")

st.markdown("""
Welcome to the **AI Resume Analyzer**.

This application will:
- 📄 Read PDF resumes
- 🧠 Extract skills
- 📊 Calculate ATS score
- 💼 Compare with Job Description
- 🤖 Generate AI recommendations
""")

# Upload PDF
uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file:
    st.success(f"File uploaded successfully: {uploaded_file.name}")