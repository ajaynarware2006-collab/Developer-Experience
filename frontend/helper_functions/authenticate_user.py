import streamlit as st

def check_user():
    user_id = st.session_state.get(
        "user_id"
    )

    if not user_id:

        st.session_state["page"] = "login"

        st.rerun()

    return user_id