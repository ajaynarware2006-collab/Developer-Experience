import streamlit as st

from utils.constants import (
    APP_NAME,
    APP_TAGLINE,
    NAVIGATION,
    ACCOUNT_NAVIGATION,
)


def render_sidebar():

    sidebar_html = f"""
    <div class="devxp-custom-sidebar">

        <div class="devxp-brand">

            <div class="devxp-brand-mark">
                D
            </div>

            <div>
                <div class="devxp-brand-name">
                    {APP_NAME}
                </div>

                <div class="devxp-brand-tagline">
                    {APP_TAGLINE}
                </div>
            </div>

        </div>


        <div class="devxp-sidebar-line"></div>


        <div class="devxp-sidebar-section">
            WORKSPACE
        </div>
    """

    for item in NAVIGATION:
        sidebar_html += f"""
        <div class="devxp-nav-item">
            <span class="devxp-nav-icon">
                {item["icon"]}
            </span>

            <span>
                {item["label"]}
            </span>
        </div>
        """

    sidebar_html += """
        <div class="devxp-sidebar-section devxp-account-section">
            ACCOUNT
        </div>
    """

    for item in ACCOUNT_NAVIGATION:
        sidebar_html += f"""
        <div class="devxp-nav-item">
            <span class="devxp-nav-icon">
                {item["icon"]}
            </span>

            <span>
                {item["label"]}
            </span>
        </div>
        """

    sidebar_html += """
        <div class="devxp-sidebar-bottom">

            <div class="devxp-user-avatar">
                A
            </div>

            <div>
                <div class="devxp-user-name">
                    Ajay
                </div>

                <div class="devxp-user-role">
                    Engineering Student
                </div>
            </div>

        </div>

    </div>
    """

    st.html(sidebar_html)