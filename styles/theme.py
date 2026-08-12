import streamlit as st


def inject_global_css():

    css = """
    <style>

    /* =====================================================
       DESIGN TOKENS
       ===================================================== */

    :root {

        --bg: #E6E6E6;
        --surface: #F4F5F1;
        --surface-soft: #ECEEEA;

        --sage-dark: #404E3B;
        --sage: #7B9669;
        --sage-light: #BAC8B1;

        --teal: #6C8480;

        --text: #1F241F;
        --text-secondary: #596058;
        --text-muted: #7B837A;

        --border: #C8CEC5;
        --border-dark: #AEB7AA;

        --white: #FFFFFF;

    }


    /* =====================================================
       APP
       ===================================================== */

    html,
    body {

        margin: 0;

        background: var(--bg);

        color: var(--text);

    }


    .stApp {

        background: var(--bg);

        color: var(--text);

    }


    [data-testid="stAppViewContainer"] {

        background: var(--bg);

    }


    [data-testid="stHeader"] {

        background: transparent;

    }


    [data-testid="stToolbar"] {

        display: none;

    }


    footer {

        visibility: hidden;

    }


    /* =====================================================
       REMOVE NATIVE STREAMLIT SIDEBAR
       ===================================================== */

    section[data-testid="stSidebar"] {

        display: none !important;

    }


    /* =====================================================
       MAIN CONTAINER
       ===================================================== */

    .block-container {
        max-width: 100%;

        padding-top: 1.25rem;
        padding-bottom: 4rem;

        padding-left: 1rem;
        padding-right: 1rem;
    }


    /* =====================================================
       CUSTOM APPLICATION SHELL
       ===================================================== */

    .devxp-shell {

        display: flex;

        width: 100%;

        min-height: calc(100vh - 3rem);

        gap: 1.5rem;

    }


    /* =====================================================
       CUSTOM SIDEBAR
       ===================================================== */

    .devxp-custom-sidebar {
        width: 100%;
        min-width: 0;
        min-height: calc(100vh - 3rem);

        box-sizing: border-box;

        padding: 1.15rem 0.9rem;

        background: var(--sage-dark);

        border-radius: 14px;

        box-shadow:
            0 8px 30px rgba(31, 36, 31, 0.10);

        display: flex;

        flex-direction: column;
    }


    /* =====================================================
       BRAND
       ===================================================== */

    .devxp-brand {

        display: flex;

        align-items: center;

        gap: 10px;

        padding: 0.25rem 0.3rem 1rem;

    }


    .devxp-brand-mark {

        width: 38px;
        height: 38px;

        display: flex;

        align-items: center;

        justify-content: center;

        flex-shrink: 0;

        background: var(--sage-light);

        color: var(--sage-dark);

        border-radius: 10px;

        font-size: 0.95rem;

        font-weight: 800;

    }


    .devxp-brand-name {

        color: var(--white);

        font-size: 0.98rem;

        font-weight: 750;

        letter-spacing: -0.02rem;

    }


    .devxp-brand-tagline {

        margin-top: 3px;

        color: var(--sage-light);

        font-family: monospace;

        font-size: 0.55rem;

    }


    .devxp-sidebar-line {

        height: 1px;

        width: 100%;

        background: #596750;

        margin-bottom: 1rem;

    }


    /* =====================================================
       SECTION LABEL
       ===================================================== */

    .devxp-sidebar-section {

        padding: 0 0.35rem;

        margin: 0.8rem 0 0.45rem;

        color: var(--sage-light);

        font-family: monospace;

        font-size: 0.55rem;

        font-weight: 600;

        letter-spacing: 0.12rem;

    }


    .devxp-account-section {

        margin-top: 1.4rem;

    }


    /* =====================================================
       NAVIGATION
       ===================================================== */

    .devxp-nav-item {

        display: flex;

        align-items: center;

        gap: 10px;

        min-height: 38px;

        box-sizing: border-box;

        padding: 0.55rem 0.7rem;

        margin: 2px 0;

        border: 1px solid transparent;

        border-radius: 8px;

        color: #E8ECE6;

        font-size: 0.72rem;

        font-weight: 500;

        transition:
            background 0.16s ease,
            border-color 0.16s ease,
            transform 0.16s ease;

    }


    .devxp-nav-item:hover {

        background: #596750;

        border-color: #6B7864;

        transform: translateX(2px);

    }


    .devxp-nav-icon {

        width: 18px;

        color: var(--sage-light);

        text-align: center;

        font-size: 0.72rem;

    }


    /* =====================================================
       USER
       ===================================================== */

    .devxp-sidebar-bottom {

        display: flex;

        align-items: center;

        gap: 10px;

        margin-top: auto;

        padding: 1rem 0.35rem 0;

        border-top: 1px solid #596750;

    }


    .devxp-user-avatar {

        width: 34px;
        height: 34px;

        display: flex;

        align-items: center;

        justify-content: center;

        flex-shrink: 0;

        background: var(--sage-light);

        color: var(--sage-dark);

        border-radius: 50%;

        font-size: 0.65rem;

        font-weight: 800;

    }


    .devxp-user-name {

        color: var(--white);

        font-size: 0.7rem;

        font-weight: 650;

    }


    .devxp-user-role {

        margin-top: 2px;

        color: var(--sage-light);

        font-size: 0.55rem;

    }


    /* =====================================================
       HEADER
       ===================================================== */

    .devxp-header {

        display: flex;

        align-items: center;

        justify-content: space-between;

        width: 100%;

        padding-bottom: 0.9rem;

        margin-bottom: 2rem;

        border-bottom: 1px solid var(--border);

    }


    .devxp-header-title {

        color: var(--text);

        font-size: 0.78rem;

        font-weight: 650;

    }


    .devxp-header-right {

        display: flex;

        align-items: center;

        gap: 0.5rem;

    }


    /* =====================================================
       SEARCH
       ===================================================== */

    .devxp-search {

        width: 205px;

        display: flex;

        align-items: center;

        gap: 7px;

        padding: 7px 9px;

        background: var(--surface);

        border: 1px solid var(--border);

        border-radius: 7px;

        box-sizing: border-box;

        color: var(--text-muted);

        font-size: 0.62rem;

    }


    .devxp-search-placeholder {

        flex: 1;

    }


    .devxp-search-key {

        padding: 2px 5px;

        background: var(--surface-soft);

        border: 1px solid var(--border);

        border-radius: 4px;

        font-family: monospace;

        font-size: 0.48rem;

    }


    /* =====================================================
       HEADER ICONS
       ===================================================== */

    .devxp-icon-button {

        width: 31px;
        height: 31px;

        display: flex;

        align-items: center;

        justify-content: center;

        background: var(--surface);

        border: 1px solid var(--border);

        border-radius: 7px;

        color: var(--text-secondary);

    }


    .devxp-header-avatar {

        width: 31px;
        height: 31px;

        display: flex;

        align-items: center;

        justify-content: center;

        background: var(--sage-dark);

        color: var(--white);

        border-radius: 50%;

        font-size: 0.58rem;

        font-weight: 700;

    }


    /* =====================================================
       PAGE
       ===================================================== */

    .devxp-eyebrow {

        color: var(--text-muted);

        font-family: monospace;

        font-size: 0.58rem;

        letter-spacing: 0.15rem;

    }


    .devxp-page-title {

        margin-top: 0.35rem;

        color: var(--text);

        font-size: 2.4rem;

        font-weight: 700;

        line-height: 1.05;

        letter-spacing: -0.07rem;

    }


    .devxp-page-description {

        max-width: 650px;

        margin-top: 0.6rem;

        color: var(--text-secondary);

        font-size: 0.82rem;

        line-height: 1.6;

    }


    /* =====================================================
       CARDS
       ===================================================== */

    .devxp-card {

        padding: 1.2rem;

        background: var(--surface);

        border: 1px solid var(--border);

        border-radius: 12px;

        box-shadow:
            0 5px 20px rgba(31, 36, 31, 0.035);

    }

    .devxp-brand-mark {
        width: 44px;
        height: 44px;

        font-size: 1.05rem;
    }

    .devxp-brand-name {
        font-size: 1.05rem;
    }

    .devxp-brand-tagline {
        font-size: 0.62rem;
    }


    .devxp-sidebar-section {
        font-size: 0.62rem;
        margin: 1rem 0 0.6rem;
    }


    .devxp-nav-item {
        min-height: 46px;

        padding: 0.65rem 0.8rem;

        font-size: 0.82rem;

        gap: 12px;
    }


    .devxp-nav-icon {
        width: 20px;

        font-size: 0.8rem;
    }


    .devxp-user-avatar {
        width: 40px;
        height: 40px;

        font-size: 0.72rem;
    }


    .devxp-user-name {
        font-size: 0.78rem;
    }


    .devxp-user-role {
        font-size: 0.62rem;
    }

    /* =====================================================
       RESPONSIVE
       ===================================================== */

    @media (max-width: 850px) {

        .devxp-shell {

            flex-direction: column;

        }

        .devxp-custom-sidebar {

            width: 100%;

            min-width: 0;

            min-height: auto;

        }

        .devxp-sidebar-bottom {

            margin-top: 1rem;

        }

    }


    </style>
    """

    st.html(css)