import streamlit as st
from services.auth_service import authenticate_user
from services.session_service import login_user

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

    left, center, right = st.columns([1.2, 2.2, 1.2])

    with center:

        with st.container(key="auth-card"):

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

            forgot_col1, forgot_col2 = st.columns([3, 1])

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

                try:

                    user = authenticate_user(
                        email=email,
                        password=password,
                    )

                    if user is None:

                        st.error(
                            "Invalid email or password."
                        )

                    else:

                        login_user(user)

                        st.session_state["page"] = "onboarding"

                        st.rerun()

                except Exception:

                    st.error(
                        "Unable to login right now. Please try again."
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