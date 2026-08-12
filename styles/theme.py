COLORS = {
    "bg": "#E6E6E6",
    "surface": "#F1F2EE",
    "surface_alt": "#E9EBE6",
    "surface_soft": "#DFE4DC",

    "primary": "#7B9669",
    "primary_dark": "#404E3B",
    "secondary": "#6C8480",
    "soft_green": "#BAC8B1",

    "border": "#C8CEC5",
    "border_hover": "#AEB7AA",

    "text": "#1F241F",
    "text_secondary": "#596058",
    "text_muted": "#7B837A",

    "white": "#FFFFFF",
}


def inject_global_css():
    import streamlit as st

    st.markdown(
        f"""
        <style>

        /* =====================================
           GLOBAL
        ===================================== */

        .stApp {{
            background: {COLORS["bg"]};
            color: {COLORS["text"]};
        }}

        .main {{
            background: {COLORS["bg"]};
        }}

        .block-container {{
            max-width: 1450px;
            padding-top: 2rem;
            padding-bottom: 4rem;
        }}

        /* Remove Streamlit default header */

        header {{
            visibility: hidden;
        }}

        /* =====================================
           TYPOGRAPHY
        ===================================== */

        h1, h2, h3, h4 {{
            color: {COLORS["text"]} !important;
            font-family: "DM Sans", sans-serif;
        }}

        p, span, label {{
            font-family: "DM Sans", sans-serif;
        }}

        /* =====================================
           SIDEBAR
        ===================================== */

        section[data-testid="stSidebar"] {{
            background: {COLORS["surface_soft"]};
            border-right: 1px solid {COLORS["border"]};
        }}

        section[data-testid="stSidebar"] > div {{
            padding-top: 1.5rem;
        }}

        /* =====================================
           BUTTONS
        ===================================== */

        .stButton > button {{
            border-radius: 7px;
            border: 1px solid {COLORS["primary_dark"]};
            background: {COLORS["primary_dark"]};
            color: white;
            font-weight: 600;
            font-size: 12px;
            padding: 0.55rem 1rem;
            transition: all 0.18s ease;
        }}

        .stButton > button:hover {{
            background: {COLORS["primary"]};
            border-color: {COLORS["primary"]};
            color: white;
        }}

        /* =====================================
           INPUTS
        ===================================== */

        .stTextInput input,
        .stSelectbox div[data-baseweb="select"] {{
            background: {COLORS["surface"]};
            border-color: {COLORS["border"]};
            border-radius: 7px;
        }}

        .stTextInput input:focus {{
            border-color: {COLORS["primary"]};
        }}

        /* =====================================
           CARDS
        ===================================== */

        .devxp-card {{
            background: {COLORS["surface"]};
            border: 1px solid {COLORS["border"]};
            border-radius: 10px;
            padding: 1.25rem;
            box-shadow:
                0 1px 2px rgba(31, 36, 31, 0.04),
                0 8px 25px rgba(31, 36, 31, 0.025);
        }}

        /* =====================================
           METRICS
        ===================================== */

        .devxp-metric {{
            background: {COLORS["surface"]};
            border: 1px solid {COLORS["border"]};
            border-radius: 10px;
            padding: 1.2rem;
        }}

        .devxp-metric-label {{
            color: {COLORS["text_muted"]};
            font-size: 0.7rem;
            letter-spacing: 0.08rem;
            text-transform: uppercase;
        }}

        .devxp-metric-value {{
            color: {COLORS["text"]};
            font-size: 1.7rem;
            font-weight: 600;
            margin-top: 0.4rem;
        }}

        .devxp-metric-change {{
            color: {COLORS["primary_dark"]};
            font-size: 0.7rem;
            margin-top: 0.2rem;
        }}

        /* =====================================
           PAGE HEADER
        ===================================== */

        .devxp-eyebrow {{
            color: {COLORS["text_muted"]};
            font-family: monospace;
            font-size: 0.65rem;
            letter-spacing: 0.12rem;
            text-transform: uppercase;
        }}

        .devxp-title {{
            color: {COLORS["text"]};
            font-size: 2.4rem;
            font-weight: 600;
            letter-spacing: -0.08rem;
            margin: 0.25rem 0;
        }}

        .devxp-subtitle {{
            color: {COLORS["text_secondary"]};
            font-size: 0.85rem;
        }}

        /* =====================================
           PROGRESS
        ===================================== */

        .progress-track {{
            width: 100%;
            height: 5px;
            background: #D5DBD1;
            border-radius: 5px;
            overflow: hidden;
        }}

        .progress-fill {{
            height: 100%;
            background: {COLORS["primary"]};
            border-radius: 5px;
        }}

        /* =====================================
           STATUS
        ===================================== */

        .devxp-badge {{
            display: inline-block;
            padding: 0.25rem 0.5rem;
            border-radius: 5px;
            background: rgba(186, 200, 177, 0.45);
            color: {COLORS["primary_dark"]};
            font-size: 0.65rem;
            font-weight: 600;
        }}

        /* =====================================
           DIVIDER
        ===================================== */

        .devxp-divider {{
            height: 1px;
            background: {COLORS["border"]};
            margin: 1.2rem 0;
        }}

        </style>
        """,
        unsafe_allow_html=True,
    )