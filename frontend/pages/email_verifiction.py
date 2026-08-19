import streamlit as st

from backend.services.verification_service import (
    verify_email_code,
)


def render_email_verification():

    user_id = st.session_state.get(
        "verification_user_id"
    )

    email = st.session_state.get(
        "verification_email"
    )

    if not user_id or not email:

        st.session_state["page"] = "signup"

        st.rerun()

    st.markdown(
        "<h1 style='text-align:center;'>"
        "Verify your email"
        "</h1>",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <p style="
            text-align:center;
            color:#91A5AA;
        ">
            We sent a verification code to
            <strong>{email}</strong>
        </p>
        """,
        unsafe_allow_html=True,
    )

    code = st.text_input(
        "Verification code",
        max_chars=6,
        placeholder="Enter 6-digit code",
    )

    if st.button(
        "Verify Email",
        type="primary",
        use_container_width=True,
    ):

        if len(code.strip()) != 6:

            st.error(
                "Enter the 6-digit verification code."
            )

            st.stop()

        success, message = (
            verify_email_code(
                user_id,
                code,
            )
        )

        if not success:

            st.error(message)

            st.stop()

        st.success(message)

        st.session_state[
            "verification_user_id"
        ] = None

        st.session_state[
            "verification_email"
        ] = None

        st.session_state[
            "page"
        ] = "login"

        st.rerun()