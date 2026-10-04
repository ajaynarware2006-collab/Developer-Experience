import streamlit as st

from frontend.styles.theme import load_theme

from frontend.components.helper import get_current_page

from frontend.pages.landing import render_landing
from frontend.pages.login import render_login
from frontend.pages.signup import render_signup
from frontend.pages.onboarding import render_onboarding
from frontend.pages.profile import render_profile
from frontend.pages.roadmap import render_roadmap
from frontend.pages.dashboard import render_dashboard
from frontend.pages.email_verifiction import render_email_verification
from frontend.pages.features import render_features
from frontend.pages.how_it_work import render_how_it_works
from frontend.pages.about import render_about


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="DEV/XP",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ============================================================
# SESSION INITIALIZATION
# ============================================================

if "page" not in st.session_state:

    st.session_state["page"] = (
        get_current_page()
    )


if "is_authenticated" not in st.session_state:

    st.session_state[
        "is_authenticated"
    ] = False


# ============================================================
# OAUTH CALLBACK
# ============================================================

auth_token = st.query_params.get(
    "auth_token"
)

oauth_page = st.query_params.get(
    "page"
)


if (
    auth_token
    and oauth_page == "dashboard"
):

    # Store token in Streamlit session.
    st.session_state[
        "access_token"
    ] = auth_token

    st.session_state[
        "is_authenticated"
    ] = True

    st.session_state[
        "page"
    ] = "dashboard"

    # Remove token from browser URL.
    st.query_params.clear()

    st.query_params["page"] = "dashboard"

    st.rerun()


# ============================================================
# PAGE FROM QUERY PARAM
# ============================================================

if "page" in st.query_params:

    requested_page = st.query_params.get(
        "page"
    )

    if requested_page:

        st.session_state[
            "page"
        ] = requested_page


# ============================================================
# PROTECTED PAGES
# ============================================================

PROTECTED_PAGES = {
    "onboarding",
    "profile",
    "roadmap",
    "dashboard",
}


if (
    st.session_state["page"]
    in PROTECTED_PAGES
    and not st.session_state[
        "is_authenticated"
    ]
):

    st.session_state[
        "page"
    ] = "login"

    st.query_params["page"] = "login"

    st.rerun()


# ============================================================
# THEME
# ============================================================

load_theme()


# ============================================================
# ROUTING
# ============================================================

pages = {

    "landing": render_landing,

    "login": render_login,

    "signup": render_signup,

    "onboarding": render_onboarding,

    "profile": render_profile,

    "roadmap": render_roadmap,

    "dashboard": render_dashboard,

    "email_verification":
        render_email_verification,

    "features":
        render_features,

    "how_it_work":
        render_how_it_works,

    "about":
        render_about,
}


current_page = st.session_state[
    "page"
]


pages[current_page]()