import streamlit as st

from analyzer.pdf_reader import extract_text
from analyzer.job_reader import extract_job_description
from analyzer.skills_extractor import load_skills, extract_skills
from analyzer.scorer import calculate_ats_score
from analyzer.similarity import calculate_similarity
from analyzer.recommendations import generate_recommendations

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

st.divider()

# --------------------------------------------------
# Resume Upload
# --------------------------------------------------

st.subheader("📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Upload your Resume (PDF)",
    type=["pdf"]
)

st.divider()

# --------------------------------------------------
# Job Description
# --------------------------------------------------

st.subheader("💼 Job Description")

job_option = st.radio(
    "Choose Job Description Input",
    (
        "Paste Text",
        "Upload PDF"
    )
)

job_description = ""

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

        job_description = extract_job_description(
            uploaded_job
        )

        st.success(
            "Job Description uploaded successfully!"
        )

st.divider()

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
        # --------------------------------------------------
    # Display Detected Skills
    # --------------------------------------------------

    st.subheader("🧠 Detected Skills")

    if detected_skills:

        cols = st.columns(3)

        for index, skill in enumerate(detected_skills):
            cols[index % 3].success(skill)

    else:

        st.warning("No skills detected.")

    st.divider()

    # --------------------------------------------------
    # ATS Score + Similarity
    # --------------------------------------------------

    if job_description.strip() != "":

        # ATS Score
        score, matched_skills, missing_skills = calculate_ats_score(
            detected_skills,
            job_description,
            skills_database
        )

        # Similarity Score
        similarity_score = calculate_similarity(
            resume_text,
            job_description
        )

        # ===============================
        # Dashboard
        # ===============================

        col1, col2 = st.columns(2)

        with col1:

            st.subheader("📊 ATS Score")

            st.metric(
                "Resume Match",
                f"{score}%"
            )

            st.progress(score / 100)

        with col2:

            st.subheader("📄 Text Similarity")

            st.metric(
                "Similarity Score",
                f"{similarity_score}%"
            )

            st.progress(similarity_score / 100)

        # ===============================
        # ATS Feedback
        # ===============================

        if score >= 80:

            st.success(
                "Excellent match! Your resume fits the job description."
            )

        elif score >= 60:

            st.info(
                "Good match. Add a few missing skills to improve your score."
            )

        else:

            st.warning(
                "Low match. Your resume needs improvements."
            )

        st.divider()
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

        st.divider()

        # --------------------------------------------------
        # AI Recommendations
        # --------------------------------------------------

        recommendations = generate_recommendations(
            score,
            matched_skills,
            missing_skills,
            resume_text
        )

        st.subheader("🤖 AI Recommendations")

        for recommendation in recommendations:
            st.info(recommendation)

    else:

        st.info("Please provide a Job Description.")