import streamlit as st
if not st.session_state.get("logged_in"):

    st.warning("🔒 Please login first.")

    st.stop()
from database.history import save_analysis
from analyzer.pdf_reader import extract_text
from analyzer.job_reader import extract_job_description
from analyzer.ai_skill_extractor import extract_skills_ai
from analyzer.ai_matcher import match_resume

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="AI Resume Analyzer AI",
    page_icon="🤖",
    layout="wide"
)

# --------------------------------------------------
# Header
# --------------------------------------------------

st.title("🤖 AI Resume Analyzer")

st.markdown("""
Analyze your Resume using **Google Gemini AI**.

### Features

- 📄 Upload Resume
- 💼 Upload Job Description
- 🤖 AI Skill Extraction
- 📊 AI Job Matching
""")

st.divider()

# --------------------------------------------------
# Upload Resume
# --------------------------------------------------

st.subheader("📄 Upload Resume")

uploaded_file = st.file_uploader(
    "Choose your Resume (PDF)",
    type=["pdf"]
)

st.divider()

# --------------------------------------------------
# Job Description
# --------------------------------------------------

st.subheader("💼 Job Description")

job_option = st.radio(
    "Choose input method",
    [
        "Paste Text",
        "Upload PDF"
    ]
)

job_description = ""

if job_option == "Paste Text":

    job_description = st.text_area(
        "Paste Job Description",
        height=200
    )

else:

    uploaded_job = st.file_uploader(
        "Upload Job Description PDF",
        type=["pdf"],
        key="job_pdf"
    )

    if uploaded_job is not None:

        job_description = extract_job_description(
            uploaded_job
        )

        st.success(
            "Job Description uploaded successfully."
        )

st.divider()

# --------------------------------------------------
# Resume Analysis
# --------------------------------------------------

if uploaded_file is not None:

    st.success("Resume uploaded successfully!")

    resume_text = extract_text(uploaded_file)

    st.subheader("📄 Resume Content")

    st.text_area(
        "",
        resume_text,
        height=300
    )

    st.divider()
        # --------------------------------------------------
    # AI Skill Extraction
    # --------------------------------------------------

    if st.button("🤖 Extract Skills with Gemini"):

        with st.spinner("Gemini is analyzing your resume..."):

            try:

                skills_data = extract_skills_ai(resume_text)

                st.success("Analysis completed!")

                st.subheader("🧠 AI Detected Skills")

                if isinstance(skills_data, dict):

                    for category, skills in skills_data.items():

                        if skills:

                            st.markdown(f"### 📂 {category}")

                            cols = st.columns(3)

                            for index, skill in enumerate(skills):

                                cols[index % 3].success(skill)

                else:

                    st.error("Invalid response from Gemini.")

            except Exception as e:

                st.error(f"Error: {e}")

    st.divider()
        # --------------------------------------------------
    # AI Job Matching
    # --------------------------------------------------

    if job_description.strip() != "":

        if st.button("📊 Analyze Resume Match"):

            with st.spinner("Gemini is comparing Resume with Job Description..."):

                try:

                    result = match_resume(
                        resume_text,
                        job_description
                    )
                    save_analysis(
                    st.session_state["user"],
                    result
                    )

                    if isinstance(result, dict):

                        st.divider()

                        st.subheader("📊 AI Job Matching")

                        col1, col2 = st.columns(2)

                        with col1:

                            st.metric(
                                "ATS Score",
                                f"{result.get('ats_score', 0)}%"
                            )

                        with col2:

                            st.metric(
                                "Similarity Score",
                                f"{result.get('similarity_score', 0)}%"
                            )

                        st.divider()

                        # --------------------------
                        # Matched Skills
                        # --------------------------

                        st.subheader("✅ Matched Skills")

                        matched = result.get("matched_skills", [])

                        if matched:

                            cols = st.columns(3)

                            for index, skill in enumerate(matched):

                                cols[index % 3].success(skill)

                        else:

                            st.info("No matched skills.")

                        # --------------------------
                        # Missing Skills
                        # --------------------------

                        st.subheader("❌ Missing Skills")

                        missing = result.get("missing_skills", [])

                        if missing:

                            cols = st.columns(3)

                            for index, skill in enumerate(missing):

                                cols[index % 3].error(skill)

                        else:

                            st.success("No missing skills.")

                        st.divider()

                        # --------------------------
                        # Recommendations
                        # --------------------------

                        st.subheader("🤖 AI Recommendations")

                        recommendations = result.get(
                            "recommendations",
                            []
                        )

                        if recommendations:

                            for rec in recommendations:

                                st.info(rec)

                        else:

                            st.success("No recommendations.")

                    else:

                        st.error("Gemini returned an invalid response.")

                except Exception as e:

                    st.error(e)

    else:

        st.info("Please provide a Job Description.")