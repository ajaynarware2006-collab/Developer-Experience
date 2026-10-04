import streamlit as st

from frontend.api.varification_api import send_verification_code
from frontend.api.login_api import authenticate_user_api
from frontend.api.user_api import get_profile


BACKEND_URL = "http://127.0.0.1:8000"


def github_login():

    st.link_button(
        "Continue with GitHub",
        "http://127.0.0.1:8000/devxp/auth/github",
        use_container_width=True,
    )


def google_login():

    st.link_button(
        "Continue with Google",
        "http://127.0.0.1:8000/devxp/auth/google",
        use_container_width=True,
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
            st.query_params["page"] = "landing"

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

            if "account_created" not in st.session_state:
                st.session_state["account_created"] = False

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

                    user = authenticate_user_api(
                        email=email,
                        password=password,
                    )

                    if user and user.get("access_token"):

                        st.session_state["access_token"] = user[
                            "access_token"
                        ]

                    if user is None:

                        st.error(
                            "Invalid email or password."
                        )

                        st.stop()

                    # --------------------------------------------
                    # CREATE SESSION
                    # --------------------------------------------

                    if not user["email_verified"]:

                        send_verification_code(email=user["email"] , user_id= user["id"])
                        st.session_state["send_verification_code"] = True

                        st.session_state["verification_user_id"] = user["id"]
                        st.session_state["verification_email"] = user["email"]
                        st.session_state["page"] = "email_verification"
                        st.query_params["page"] = "email_verification"

                        st.warning(
                            "Your email is not verified. A new verification code has been sent."
                        )

                        st.rerun()


                    st.session_state["is_authenticated"] = True
                    st.session_state["user_id"] = user["id"]
                    st.session_state["user_name"] = user["name"]
                    st.session_state["user_email"] = user["email"]

                    # --------------------------------------------
                    # LOAD PROFILE FROM DATABASE
                    # --------------------------------------------

                    profile = get_profile(
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
            # SOCIAL LOGINS
            # ----------------------------------------------------

            google_col, github_col = st.columns(2)

            with google_col:

                google_login()

            with github_col:

                github_login()

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
                st.query_params["page"] = "signup"

                st.rerun()