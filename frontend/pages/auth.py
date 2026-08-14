import streamlit as st


def render_auth(mode):

    is_signup = mode == "signup"

    # ============================================================
    # PAGE HEADER
    # ============================================================

    if st.button(
        "← Back",
        key=f"{mode}_back",
    ):
        st.session_state["page"] = "landing"
        st.rerun()


    # ============================================================
    # AUTH CARD
    # ============================================================

    left, center, right = st.columns([1, 2, 1])

    with center:

        with st.container(border=True,key="auth-card"):

            # --------------------------------------------------------
            # CARD HEADER
            # --------------------------------------------------------

            st.html(
                f"""
                <div class="auth-card-header">

                    <div class="auth-title">
                        {
                            "Create your account"
                            if is_signup
                            else
                            "Welcome back"
                        }
                    </div>

                    <div class="auth-subtitle">

                        {
                            "Start building your personalized developer journey."
                            if is_signup
                            else
                            "Sign in to continue your developer journey."
                        }

                    </div>

                </div>
                """
            )


            # --------------------------------------------------------
            # FORM
            # --------------------------------------------------------

            if is_signup:

                name = st.text_input(
                    "Full Name",
                    placeholder="Enter your name",
                    key="signup_name",
                )

                email = st.text_input(
                    "Email",
                    placeholder="you@example.com",
                    key="signup_email",
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Create a password",
                    key="signup_password",
                )

                confirm_password = st.text_input(
                    "Confirm Password",
                    type="password",
                    placeholder="Confirm your password",
                    key="signup_confirm_password",
                )


                # ----------------------------------------------------
                # SIGNUP BUTTON
                # ----------------------------------------------------

                if st.button(
                    "Create Account",
                    type="primary",
                    use_container_width=True,
                    key="signup_submit",
                ):

                    if not name or not email or not password:
                        st.error(
                            "Please complete all required fields."
                        )

                    elif password != confirm_password:
                        st.error(
                            "Passwords do not match."
                        )

                    else:
                        st.success(
                            "Account form submitted."
                        )


                # ----------------------------------------------------
                # LOGIN SWITCH
                # ----------------------------------------------------

                st.html(
                    """
                    <div class="auth-switch-label">
                        Already have an account?
                    </div>
                    """
                )


                if st.button(
                    "Sign In",
                    use_container_width=True,
                    key="signup_to_login",
                ):
                    st.session_state["page"] = "login"
                    st.rerun()


            else:

                email = st.text_input(
                    "Email",
                    placeholder="you@example.com",
                    key="login_email",
                )

                password = st.text_input(
                    "Password",
                    type="password",
                    placeholder="Enter your password",
                    key="login_password",
                )


                # ----------------------------------------------------
                # LOGIN BUTTON
                # ----------------------------------------------------

                if st.button(
                    "LOGIN",
                    type="primary",
                    use_container_width=True,
                    key="login_submit",
                ):

                    if not email or not password:
                        st.error(
                            "Please enter your email and password."
                        )

                    else:
                        st.success(
                            "Login form submitted."
                        )


                # ----------------------------------------------------
                # SIGNUP SWITCH
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
                    key="login_to_signup",
                ):
                    st.session_state["page"] = "signup"
                    st.rerun()