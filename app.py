import streamlit as st

from analyzer.pdf_reader import extract_text
from analyzer.job_reader import extract_job_description
from analyzer.skills_extractor import load_skills, extract_skills
from analyzer.scorer import calculate_ats_score
from analyzer.similarity import calculate_similarity

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
# Resume Upload
# --------------------------------------------------

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

# --------------------------------------------------
# Job Description
# --------------------------------------------------

st.subheader("💼 Job Description")

job_option = st.radio(
    "Choose Job Description Input",
    ["Paste Text", "Upload PDF"]
)

if job_option == "Paste Text":

    job_description = st.text_area(
        "Paste the Job Description",
        height=200
    )

else:

    uploaded_job = st.file_uploader(
        "Upload Job Description (PDF)",
        type=["pdf"],
        key="job_pdf"
    )

    if uploaded_job is not None:

        job_description = extract_job_description(uploaded_job)

        st.success("Job Description uploaded successfully!")

    else:

        job_description = ""

# --------------------------------------------------
# Resume Analysis
# --------------------------------------------------

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    # Extract Resume Text
    resume_text = extract_text(uploaded_file)

    # Display Resume
    st.subheader("📄 View Extracted Resume")

    st.text_area(
        "Resume Content",
        resume_text,
        height=300
    )

    # Load Skills Database
    skills_database = load_skills()

    # Detect Skills
    detected_skills = extract_skills(
        resume_text,
        skills_database
    )

    # Display Skills
    st.subheader("🧠 Detected Skills")

    if detected_skills:

        cols = st.columns(3)

        for index, skill in enumerate(detected_skills):
            cols[index % 3].success(skill)

    else:

        st.warning("No skills detected.")

    # --------------------------------------------------
    # ATS + Similarity
    # --------------------------------------------------

    if job_description.strip() != "":

        score, matched_skills, missing_skills = calculate_ats_score(
            detected_skills,
            job_description,
            skills_database
        )

        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # ATS Score

        st.subheader("📊 ATS Score")

        st.metric(
            "Resume Match",
            f"{score}%"
        )

        st.progress(score / 100)

        if score >= 80:

            st.success(
                "Excellent match! Your resume fits the job description."
            )

        elif score >= 60:

            st.info(
                "Good match. Consider adding the missing skills."
            )

        else:

            st.warning(
                "Low match. Update your resume to better fit the job description."
            )

        # --------------------------------------------------
        # Text Similarity
        # --------------------------------------------------

        st.subheader("📄 Text Similarity")

        st.metric(
            "Similarity Score",
            f"{similarity_score}%"
        )

        st.progress(similarity_score / 100)

        # --------------------------------------------------
        # Matched Skills
        # --------------------------------------------------

        st.subheader("✅ Matched Skills")

        if matched_skills:

            cols = st.columns(3)

            for index, skill in enumerate(matched_skills):
                cols[index % 3].success(skill)

        else:

            st.info("No matched skills found.")

        # --------------------------------------------------
        # Missing Skills
        # --------------------------------------------------

        st.subheader("❌ Missing Skills")

        if missing_skills:

            cols = st.columns(3)

            for index, skill in enumerate(missing_skills):
                cols[index % 3].error(skill)

        else:

            st.success("No missing skills!")

    else:

        st.info("Please provide a Job Description.")