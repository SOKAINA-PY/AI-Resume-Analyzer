import streamlit as st

from database.profile import get_profile
from database.history_reader import get_history

st.set_page_config(
    page_title="Profile",
    page_icon="👤",
    layout="wide"
)

if not st.session_state.get("logged_in"):
    st.warning("🔒 Please Login First")
    st.stop()

profile = get_profile(
    st.session_state["user"]
)

history = get_history(
    st.session_state["user"]
)

st.title("👤 My Profile")

st.divider()

col1, col2 = st.columns(2)

with col1:

    st.metric(
        "📧 Email",
        profile["email"]
    )

with col2:

    st.metric(
        "📅 Member Since",
        profile["created_at"][:10]
    )

st.divider()

total = len(history)

if total > 0:

    average = sum(
        item["ats_score"] for item in history
    ) / total

    best = max(
        item["ats_score"] for item in history
    )

else:

    average = 0
    best = 0

col1, col2, col3 = st.columns(3)

with col1:

    st.metric(
        "📊 Analyses",
        total
    )

with col2:

    st.metric(
        "🏆 Best ATS",
        f"{best}%"
    )

with col3:

    st.metric(
        "⭐ Average ATS",
        f"{average:.1f}%"
    )

st.divider()

if st.button("🚪 Logout"):

    st.session_state.clear()

    st.rerun()