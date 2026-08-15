import streamlit as st

from styles.theme import load_theme
from components.navbar import render_navbar
from pages.landing import render_landing
from pages.login import render_login
from pages.signup import render_signup
from pages.auth import render_auth
from pages.onboarding import render_onboarding
from pages.profile import render_profile
from pages.roadmap import render_roadmap
from pages.dashboard import render_dashboard

# ============================================================
# PAGE CONFIG
# ============================================================
def is_authenticated():

    return st.session_state.get(
        "is_authenticated",
        False,
    )

PROTECTED_PAGES = {
    "onboarding",
    "profile",
    "roadmap",
    "dashboard",
}

current_page = st.session_state.get(
    "page",
    "landing",
)


if (
    current_page in PROTECTED_PAGES
    and not is_authenticated()
):

    st.session_state["page"] = "login"

    st.rerun()

st.set_page_config(
    page_title="DEV/XP",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="collapsed",
)


# ============================================================
# THEME
# ============================================================

load_theme()


# ============================================================
# SESSION STATE
# ============================================================

if "page" not in st.session_state:
    st.session_state["page"] = "landing"


# ============================================================
# NAVBAR
# ============================================================

render_navbar()


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
}

current_page = st.session_state["page"]

pages[current_page]()

