import streamlit as st
from frontend.services.auth_service import register_user
from backend.services.verification_service import create_email_verification
from backend.services.email_service import send_verification_code

def render_signup():

    # ============================================================
    # BACK BUTTON
    # ============================================================

    back_col, _, _ = st.columns([1, 5, 1])

    with back_col:

        if st.button(
            "← Back",
            key="signup_back",
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
                        Create your account
                    </div>

                    <div class="auth-subtitle">
                        Start building your personalized
                        developer journey.
                    </div>

                </div>
                """
            )


            # ----------------------------------------------------
            # NAME
            # ----------------------------------------------------

            name = st.text_input(
                "Full Name",
                placeholder="Your name",
                key="signup_name",
            )


            # ----------------------------------------------------
            # EMAIL
            # ----------------------------------------------------

            email = st.text_input(
                "Email",
                placeholder="you@example.com",
                key="signup_email",
            )


            # ----------------------------------------------------
            # PASSWORD
            # ----------------------------------------------------

            password = st.text_input(
                "Password",
                placeholder="Create a strong password",
                type="password",
                key="signup_password",
            )


            # ----------------------------------------------------
            # CONFIRM PASSWORD
            # ----------------------------------------------------

            confirm_password = st.text_input(
                "Confirm Password",
                placeholder="Repeat your password",
                type="password",
                key="signup_confirm_password",
            )


            # ----------------------------------------------------
            # TERMS
            # ----------------------------------------------------

            terms = st.checkbox(
                "I agree to the Terms of Service and Privacy Policy.",
                key="signup_terms",
            )


            # ----------------------------------------------------
            # CREATE ACCOUNT
            # ----------------------------------------------------
            if "account_created" not in st.session_state:
                st.session_state.account_created = False

            if st.button(
                "Create Account",
                type="primary",
                use_container_width=True,
                key="signup_submit",
                disabled=not name or not email
            ):

                if not name or not email:
                    st.error(
                        "Please fill in all required fields."
                    )

                elif not password:
                    st.error(
                        "Please create a password."
                    )

                elif password != confirm_password:
                    st.error(
                        "Passwords do not match."
                    )

                elif len(password) < 8:
                    st.error(
                        "Password must contain at least 8 characters."
                    )

                elif not terms:
                    st.error(
                        "Please accept the Terms of Service."
                    )

                else:
                    st.session_state.account_create = True
                    try:

                        user = register_user(
                            name=name.strip(),
                            email=email.strip().lower(),
                            password=password,
                        )

                        _, code = create_email_verification(
                            user.id,
                            user.email,
                        )

                        send_verification_code(
                            user.email,
                            code,
                        )

                        st.session_state["verification_user_id"] = user.id
                        st.session_state["user_name"] = user.name
                        st.session_state["verification_email"] = user.email

                        st.session_state["page"] = "email_verification"
                        st.rerun()

                    except ValueError as error:

                        st.error(str(error))

                    except Exception:

                        st.error(
                            "Something went wrong while creating your account."
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
            # SOCIAL SIGNUP
            # ----------------------------------------------------

            google_col, github_col = st.columns(2)

            with google_col:

                st.button(
                    "Google",
                    use_container_width=True,
                    key="signup_google",
                )

            with github_col:

                st.button(
                    "GitHub",
                    use_container_width=True,
                    key="signup_github",
                )


            # ----------------------------------------------------
            # LOGIN
            # ----------------------------------------------------

            st.html(
                """
                <div class="auth-switch-label">
                    Already have an account?
                </div>
                """
            )


            if st.button(
                "LOGIN",
                use_container_width=True,
                key="signup_login",
            ):

                st.session_state["page"] = "login"
                st.rerun()