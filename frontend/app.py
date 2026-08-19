import streamlit as st

from frontend.styles.theme import load_theme
from frontend.components.navbar import render_navbar

from frontend.pages.landing import render_landing
from frontend.pages.login import render_login
from frontend.pages.signup import render_signup
from frontend.pages.onboarding import render_onboarding
from frontend.pages.profile import render_profile
from frontend.pages.roadmap import render_roadmap
from frontend.pages.dashboard import render_dashboard
from frontend.pages.email_verifiction import render_email_verification

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

    st.session_state["page"] = "landing"


if "is_authenticated" not in st.session_state:

    st.session_state[
        "is_authenticated"
    ] = False


# ============================================================
# AUTHENTICATION
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
    and not st.session_state["is_authenticated"]
):

    st.session_state["page"] = "login"

    st.rerun()


# ============================================================
# THEME
# ============================================================

load_theme()


# ============================================================
# NAVBAR
# ============================================================

render_navbar()


# ============================================================
# ROUTING
# ============================================================

pages = {

    "landing":
        render_landing,

    "login":
        render_login,

    "signup":
        render_signup,

    "onboarding":
        render_onboarding,

    "profile":
        render_profile,

    "roadmap":
        render_roadmap,

    "dashboard":
        render_dashboard,

    "email_verification":
        render_email_verification,
}


current_page = st.session_state[
    "page"
]


pages[current_page]()