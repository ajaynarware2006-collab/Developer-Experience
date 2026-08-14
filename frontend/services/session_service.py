import streamlit as st


def login_user(user: dict):

    st.session_state["is_authenticated"] = True

    st.session_state["user_id"] = user["id"]

    st.session_state["user_name"] = user["name"]

    st.session_state["user_email"] = user["email"]


def logout_user():

    keys_to_remove = [
        "is_authenticated",
        "user_id",
        "user_name",
        "user_email",
        "onboarding",
        "onboarding_step",
        "onboarding_complete",
        "editing_profile",
        "roadmap_progress",
    ]

    for key in keys_to_remove:

        st.session_state.pop(
            key,
            None,
        )

    st.session_state["page"] = "landing"