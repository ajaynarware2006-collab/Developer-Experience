import streamlit as st
import time


from frontend.api.varification_api import verify_varification_code , send_verification_code

def render_email_verification():

    name = st.session_state.get("user_name")

    user_id = st.session_state.get("verification_user_id")

    email = st.session_state.get("verification_email")

    #======================================================================

    if not user_id or not email:

        st.error("Something went wrong... User not Found")
        time.sleep(1)
        st.session_state["page"] = "signup"
        st.query_params["page"] = "signup"

        st.rerun()

    #======================================================================
    st.html(
        "<h1 style='text-align:center;'>"
        "Verify your email"
        "</h1>"
    )

    st.html(
        f"""
        <p style="
            text-align:center;
            color:#91A5AA;
        ">
            We sent a verification code to
            <strong>{email}</strong>
        </p>
        """
    )
    if "send_verification_code" not in st.session_state:
        st.session_state["send_verification_code"] = False
    try:
        if not st.session_state["send_verification_code"]:

            send_verification_code(email , user_id)
            st.session_state["send_verification_code"] = True

    except Exception as e :
        st.error(f"Email not send\n Error : {e}")
    
    #======================================================================

    _ , col , _ = st.columns([2,3,2])

    with col:
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

            success, message = verify_varification_code(
                user_id=user_id,
                entered_code= code
            )

            if not success:

                st.error(message)

                st.stop()

            st.success(message)

            st.session_state["is_authenticated"] = True

            st.session_state["user_id"] = user_id

            st.session_state["user_name"] = name

            st.session_state["user_email"] = email

            st.session_state["verification_user_id"] = None

            st.session_state["verification_email"] = None

            st.session_state["page"] = "onboarding"
            st.query_params["page"] = "onbording"

            st.rerun()