import streamlit as st

from database.history_reader import get_history

st.set_page_config(
    page_title="History",
    page_icon="📊"
)

if not st.session_state.get("logged_in"):

    st.warning("🔒 Please Login First")

    st.stop()

st.title("📊 Analysis History")

history = get_history(
    st.session_state["user"]
)

if len(history) == 0:

    st.info("No analysis found.")

else:

    for item in history:

        with st.expander(
            f"📄 ATS {item['ats_score']}% | Similarity {item['similarity_score']}%"
        ):

            st.write("### ✅ Matched Skills")

            for skill in item["matched_skills"]:
                st.success(skill)

            st.write("### ❌ Missing Skills")

            for skill in item["missing_skills"]:
                st.error(skill)

            st.write("### 🤖 Recommendations")

            for recommendation in item["recommendations"]:
                st.info(recommendation)

            st.caption(item["created_at"])