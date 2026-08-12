import streamlit as st

from styles.theme import inject_global_css
from components.layout.sidebar import render_sidebar
from components.layout.header import render_header


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="DEV/XP",
    page_icon="D",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# =========================================================
# GLOBAL CSS
# =========================================================

inject_global_css()


# =========================================================
# SESSION STATE
# =========================================================

if "current_page" not in st.session_state:
    st.session_state["current_page"] = "dashboard"


# =========================================================
# APPLICATION SHELL
# =========================================================

sidebar_column, content_column = st.columns(
    [0.85, 3.8],
    gap="large",
)


# =========================================================
# SIDEBAR
# =========================================================

with sidebar_column:

    render_sidebar()


# =========================================================
# MAIN CONTENT
# =========================================================

with content_column:

    render_header("Overview")

    st.html(
        """
        <div style="padding: 1rem 0 4rem 0;">

            <div class="devxp-eyebrow">
                DEV / XP
            </div>

            <div class="devxp-page-title">
                Welcome back, Ajay.
            </div>

            <div class="devxp-page-description">
                Your engineering growth platform.
                Track your skills, learning progress,
                projects, and development journey.
            </div>

        </div>
        """
    )