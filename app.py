import streamlit as st

from analyzer.pdf_reader import extract_text
from analyzer.skills_extractor import load_skills, extract_skills

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

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

# --------------------------------------------------
# Upload Resume
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# --------------------------------------------------
# Resume Analysis
# --------------------------------------------------

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract resume text
    resume_text = extract_text(uploaded_file)

    # Display extracted text
    st.subheader("📄 View Extracted Resume")
    st.text_area(
        "Resume Content",
        resume_text,
        height=350
    )

    # Load skills database
    skills_database = load_skills()

    # Extract skills
    detected_skills = extract_skills(
        resume_text,
        skills_database
    )

    # Display detected skills
    st.subheader("🧠 Detected Skills")

    if detected_skills:

        cols = st.columns(3)

        for index, skill in enumerate(detected_skills):
            cols[index % 3].success(f"✅ {skill}")

    else:

        st.warning("No skills were detected.")