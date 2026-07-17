import streamlit as st

from analyzer.pdf_reader import extract_text
from analyzer.job_reader import extract_job_description
from analyzer.ai_skill_extractor import extract_skills_ai

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

- 📄 Upload Resume PDF
- 💼 Upload or Paste Job Description
- 🤖 AI Skill Extraction
- 🧠 AI Powered Analysis
""")

st.divider()

# --------------------------------------------------
# Resume Upload
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
    ["Paste Text", "Upload PDF"]
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

        job_description = extract_job_description(uploaded_job)

        st.success("Job Description uploaded successfully.")

# --------------------------------------------------
# Resume Analysis
# --------------------------------------------------

if uploaded_file is not None:

    st.divider()

    st.success("Resume uploaded successfully!")

    # Read PDF

    resume_text = extract_text(uploaded_file)

    st.subheader("📄 Resume Content")

    st.text_area(
        "",
        resume_text,
        height=300
    )

    st.divider()

    # AI Button

    if st.button("🤖 Extract Skills with Gemini"):

        with st.spinner("Gemini is analyzing your resume..."):

            try:

                skills_data = extract_skills_ai(resume_text)

                st.success("Analysis completed!")

                st.write("Returned object type:")

                st.write(type(skills_data))

                st.subheader("🧠 AI Detected Skills")

                if isinstance(skills_data, dict):

                    for category, skills in skills_data.items():

                        if skills:

                            st.markdown(f"### 📂 {category}")

                            cols = st.columns(3)

                            for index, skill in enumerate(skills):

                                cols[index % 3].success(skill)

                else:

                    st.write(skills_data)

            except Exception as e:

                st.error(e)