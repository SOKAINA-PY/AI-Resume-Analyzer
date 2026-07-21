import streamlit as st

st.set_page_config(
    page_title="Profile",
    page_icon="👤"
)

if not st.session_state.get("logged_in"):
    st.warning("🔒 Please Login First")
    st.stop()

st.title("👤 My Profile")

st.write("### Email")
st.success(st.session_state["user"])