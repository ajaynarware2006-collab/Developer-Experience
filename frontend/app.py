import streamlit as st

from styles.theme import load_theme
from components.navbar import render_navbar
from pages.landing import render_landing
from pages.auth import render_auth


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

current_page = st.session_state["page"]


if current_page == "landing":

    render_landing()


elif current_page == "signup":

    render_auth("signup")


elif current_page == "login":

    render_auth("login")