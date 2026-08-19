import streamlit as st

from frontend.services.auth_service import authenticate_user
from frontend.services.session_service import login_user
from backend.repositories.profile_repository import (
    get_profile_by_user_id,
)


def render_login():

    # ============================================================
    # BACK BUTTON
    # ============================================================

    back_col, _, _ = st.columns([1, 5, 1])

    with back_col:

        if st.button(
            "← Back",
            key="login_back",
        ):

            st.session_state["page"] = "landing"

            st.rerun()

    # ============================================================
    # AUTH CARD
    # ============================================================

    left, center, right = st.columns(
        [1.2, 2.2, 1.2]
    )

    with center:

        with st.container(
            key="auth-card"
        ):

            st.html(
                """
                <div class="auth-card-header">

                    <div class="auth-title">
                        Welcome back
                    </div>

                    <div class="auth-subtitle">
                        Sign in to continue your developer journey.
                    </div>

                </div>
                """
            )

            # ----------------------------------------------------
            # EMAIL
            # ----------------------------------------------------

            email = st.text_input(
                "Email",
                placeholder="you@example.com",
                key="login_email",
            )

            # ----------------------------------------------------
            # PASSWORD
            # ----------------------------------------------------

            password = st.text_input(
                "Password",
                placeholder="Enter your password",
                type="password",
                key="login_password",
            )

            # ----------------------------------------------------
            # FORGOT PASSWORD
            # ----------------------------------------------------

            forgot_col1, forgot_col2 = st.columns(
                [3, 1]
            )

            with forgot_col2:

                if st.button(
                    "Forgot password?",
                    key="forgot_password",
                ):

                    st.info(
                        "Password recovery will be available soon."
                    )

            # ----------------------------------------------------
            # LOGIN
            # ----------------------------------------------------

            if st.button(
                "LOGIN",
                type="primary",
                use_container_width=True,
                key="login_submit",
            ):

                if not email.strip():

                    st.error(
                        "Please enter your email."
                    )

                    st.stop()

                if not password:

                    st.error(
                        "Please enter your password."
                    )

                    st.stop()

                try:

                    user = authenticate_user(
                        email=email,
                        password=password,
                    )

                    if user is None:

                        st.error(
                            "Invalid email or password."
                        )

                        st.stop()

                    # --------------------------------------------
                    # CREATE SESSION
                    # --------------------------------------------

                    if not user["email_verified"]:

                        st.warning(
                            "Please verify your email before logging in."
                        )

                        st.session_state[
                            "verification_user_id"
                        ] = user["id"]

                        st.session_state[
                            "verification_email"
                        ] = user["email"]

                        st.session_state[
                            "page"
                        ] = "email_verification"

                        st.rerun()
                    login_user(user)

                    # --------------------------------------------
                    # LOAD PROFILE FROM DATABASE
                    # --------------------------------------------

                    profile = get_profile_by_user_id(
                        user["id"]
                    )

                    if profile is None:

                        # New user / incomplete onboarding

                        st.session_state[
                            "onboarding_complete"
                        ] = False

                        st.session_state[
                            "onboarding_step"
                        ] = 1

                        st.session_state[
                            "page"
                        ] = "onboarding"

                    else:

                        # Existing user

                        st.session_state[
                            "profile_id"
                        ] = profile.id

                        st.session_state[
                            "onboarding_complete"
                        ] = True

                        st.session_state[
                            "page"
                        ] = "dashboard"

                    st.rerun()

                except Exception as error:

                    st.error(
                        f"Unable to login right now: {error}"
                    )

            # ----------------------------------------------------
            # DIVIDER
            # ----------------------------------------------------

            st.html(
                """
                <div
                    style="
                        display:flex;
                        align-items:center;
                        gap:12px;
                        margin:25px 0;
                    "
                >

                    <div
                        style="
                            flex:1;
                            height:1px;
                            background:
                                rgba(255,255,255,0.08);
                        "
                    ></div>

                    <span
                        style="
                            color:#687D82;
                            font-size:12px;
                        "
                    >
                        OR
                    </span>

                    <div
                        style="
                            flex:1;
                            height:1px;
                            background:
                                rgba(255,255,255,0.08);
                        "
                    ></div>

                </div>
                """
            )

            # ----------------------------------------------------
            # SOCIAL LOGIN PLACEHOLDERS
            # ----------------------------------------------------

            google_col, github_col = st.columns(2)

            with google_col:

                st.button(
                    "Google",
                    use_container_width=True,
                    key="login_google",
                )

            with github_col:

                st.button(
                    "GitHub",
                    use_container_width=True,
                    key="login_github",
                )

            # ----------------------------------------------------
            # SIGNUP
            # ----------------------------------------------------

            st.html(
                """
                <div class="auth-switch-label">
                    Don't have an account?
                </div>
                """
            )

            if st.button(
                "Create Account",
                use_container_width=True,
                key="login_create_account",
            ):

                st.session_state["page"] = "signup"

                st.rerun()