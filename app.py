import streamlit as st
from analyzer.pdf_reader import extract_text

# ======================================================
# Page Configuration
# ======================================================

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# ======================================================
# Title
# ======================================================

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

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    text = extract_text(uploaded_file)

    with st.expander("📄 View Extracted Resume"):
        st.text(text)