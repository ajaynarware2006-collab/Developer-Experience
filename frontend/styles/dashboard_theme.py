import streamlit as st


def load_dashboard_theme():

    st.html(
        """
        <style>

        /* =========================================================
           DASHBOARD ONLY
        ========================================================= */

        /* Hide the public navbar ONLY while dashboard is rendered */

        .devxp-navbar {
            display: none !important;
        }


        /* =========================================================
           PAGE
        ========================================================= */

        section.main > div.block-container {

            max-width: 1500px !important;

            padding:
                24px 28px 60px !important;
        }


        /* =========================================================
           REMOVE EXTRA STREAMLIT SPACE
        ========================================================= */

        .stApp {
            background:
                radial-gradient(
                    circle at 10% 10%,
                    rgba(0, 145, 155, 0.08),
                    transparent 32%
                ),
                radial-gradient(
                    circle at 90% 80%,
                    rgba(158, 211, 60, 0.045),
                    transparent 28%
                ),
                #071113 !important;
        }


        /* =========================================================
           SIDEBAR
        ========================================================= */

        .st-key-dashboard-sidebar {

            position: sticky;

            top: 20px;

            min-height: calc(100vh - 60px);

            padding:
                22px 16px;

            border-radius: 22px;

            background:
                linear-gradient(
                    145deg,
                    rgba(16, 31, 33, 0.92),
                    rgba(9, 20, 22, 0.82)
                );

            border:
                1px solid
                rgba(255,255,255,0.075);

            box-shadow:
                0 25px 70px
                rgba(0,0,0,0.28);

            backdrop-filter:
                blur(24px);

            -webkit-backdrop-filter:
                blur(24px);
        }


        /* =========================================================
           SIDEBAR BRAND
        ========================================================= */

        .dashboard-brand {

            display: flex;

            align-items: center;

            gap: 12px;

            padding:
                5px 8px 25px;

            border-bottom:
                1px solid
                rgba(255,255,255,0.055);

            margin-bottom: 22px;
        }


        .dashboard-brand-logo {

            width: 40px;

            height: 40px;

            display: flex;

            align-items: center;

            justify-content: center;

            border-radius: 12px;

            background:
                linear-gradient(
                    135deg,
                    #0B8E99,
                    #12AAB3
                );

            color: #F4F7F5;

            font-size: 17px;

            font-weight: 850;

            box-shadow:
                0 0 28px
                rgba(18,170,179,0.28);
        }


        .dashboard-brand-name {

            color: #F4F7F5;

            font-size: 18px;

            font-weight: 850;

            letter-spacing: -0.2px;
        }


        .dashboard-brand-subtitle {

            color: #60777B;

            font-size: 10px;

            margin-top: 2px;
        }


        /* =========================================================
           SIDEBAR SECTION
        ========================================================= */

        .dashboard-section-label {

            color: #50666A;

            font-size: 9px;

            font-weight: 800;

            letter-spacing: 1.7px;

            margin:
                18px 10px 8px;

            text-transform: uppercase;
        }


        /* =========================================================
           SIDEBAR BUTTONS
        ========================================================= */

        .st-key-dashboard-sidebar
        div[data-testid="stButton"] {

            margin: 3px 0 !important;
        }


        .st-key-dashboard-sidebar
        div[data-testid="stButton"] button {

            width: 100% !important;

            min-height: 43px !important;

            justify-content: flex-start !important;

            text-align: left !important;

            padding:
                0 13px !important;

            border-radius: 11px !important;

            border:
                1px solid transparent !important;

            background:
                transparent !important;

            color: #819497 !important;

            font-size: 13px !important;

            font-weight: 650 !important;

            box-shadow: none !important;

            transition:
                all 0.18s ease !important;
        }


        .st-key-dashboard-sidebar
        div[data-testid="stButton"] button:hover {

            color: #EAF2F1 !important;

            background:
                rgba(255,255,255,0.035) !important;

            border-color:
                rgba(255,255,255,0.055) !important;

            transform: translateX(2px);
        }


        .st-key-dashboard-sidebar
        div[data-testid="stButton"] button:disabled {

            color:
                #46585B !important;

            opacity:
                0.65 !important;

            cursor:
                default !important;
        }


        /* =========================================================
           ACTIVE DASHBOARD BUTTON
        ========================================================= */

        .st-key-dashboard-sidebar
        .active-nav {

            display: block;

            padding: 0;

        }


        /* =========================================================
           USER CARD
        ========================================================= */

        .dashboard-user {

            display: flex;

            align-items: center;

            gap: 10px;

            margin-top: 24px;

            padding:
                15px 8px 5px;

            border-top:
                1px solid
                rgba(255,255,255,0.055);
        }


        .dashboard-avatar {

            width: 35px;

            height: 35px;

            display: flex;

            align-items: center;

            justify-content: center;

            border-radius: 50%;

            background:
                rgba(18,170,179,0.12);

            border:
                1px solid
                rgba(18,170,179,0.22);

            color: #9EDFE3;

            font-size: 12px;

            font-weight: 800;

            flex-shrink: 0;
        }


        .dashboard-user-name {

            color: #EAF2F1;

            font-size: 12px;

            font-weight: 700;
        }


        .dashboard-user-email {

            color: #536A6E;

            font-size: 9px;

            margin-top: 2px;

            overflow: hidden;

            text-overflow: ellipsis;

            white-space: nowrap;
        }


        /* =========================================================
           MAIN HEADER
        ========================================================= */

        .dashboard-header {

            display: flex;

            align-items: center;

            justify-content: space-between;

            min-height: 58px;

            margin-bottom: 34px;

            padding:
                0 4px 18px;

            border-bottom:
                1px solid
                rgba(255,255,255,0.055);
        }


        .dashboard-header-title {

            color: #EAF2F1;

            font-size: 16px;

            font-weight: 700;
        }


        .dashboard-header-subtitle {

            color: #52686A;

            font-size: 11px;

            margin-top: 3px;
        }


        .dashboard-header-user {

            display: flex;

            align-items: center;

            gap: 10px;
        }


        .dashboard-online {

            display: flex;

            align-items: center;

            gap: 6px;

            color: #60777B;

            font-size: 10px;
        }


        .dashboard-online-dot {

            width: 6px;

            height: 6px;

            border-radius: 50%;

            background: #9ED33C;

            box-shadow:
                0 0 10px
                rgba(158,211,60,0.7);
        }


        /* =========================================================
           WELCOME
        ========================================================= */

        .dashboard-eyebrow {

            display: inline-block;

            padding:
                7px 11px;

            border-radius: 999px;

            border:
                1px solid
                rgba(158,211,60,0.18);

            background:
                rgba(158,211,60,0.045);

            color: #9ED33C;

            font-size: 9px;

            font-weight: 800;

            letter-spacing: 1.5px;

            text-transform: uppercase;
        }


        .dashboard-welcome {

            margin-bottom: 34px;
        }


        .dashboard-welcome h1 {

            margin:
                14px 0 8px;

            color: #F4F7F5;

            font-size: 42px;

            line-height: 1.08;

            letter-spacing: -1.7px;

            font-weight: 850;
        }


        .dashboard-welcome p {

            margin: 0;

            color: #81979B;

            font-size: 15px;

            line-height: 1.65;
        }


        /* =========================================================
           SECTION LABEL
        ========================================================= */

        .dashboard-content-label {

            margin-bottom: 13px;

            color: #536A6E;

            font-size: 9px;

            font-weight: 800;

            letter-spacing: 1.6px;

            text-transform: uppercase;
        }


        /* =========================================================
           STAT CARDS
        ========================================================= */

        .dashboard-stat {

            min-height: 118px;

            padding: 20px;

            border-radius: 17px;

            background:
                linear-gradient(
                    145deg,
                    rgba(19,36,38,0.76),
                    rgba(11,23,25,0.68)
                );

            border:
                1px solid
                rgba(255,255,255,0.065);

            box-shadow:
                0 15px 40px
                rgba(0,0,0,0.16);
        }


        .dashboard-stat-label {

            color: #647B7F;

            font-size: 10px;

            font-weight: 700;

            letter-spacing: 0.6px;
        }


        .dashboard-stat-value {

            margin-top: 12px;

            color: #F4F7F5;

            font-size: 20px;

            line-height: 1.15;

            font-weight: 800;
        }


        .dashboard-stat-meta {

            margin-top: 7px;

            color: #526A6E;

            font-size: 10px;
        }


        /* =========================================================
           CARDS
        ========================================================= */

        .dashboard-card {

            padding: 24px;

            border-radius: 19px;

            background:
                linear-gradient(
                    145deg,
                    rgba(18,34,36,0.74),
                    rgba(9,20,22,0.68)
                );

            border:
                1px solid
                rgba(255,255,255,0.065);

            box-shadow:
                0 20px 50px
                rgba(0,0,0,0.18);

            backdrop-filter:
                blur(18px);

            -webkit-backdrop-filter:
                blur(18px);
        }


        .dashboard-card-title {

            color: #F4F7F5;

            font-size: 19px;

            font-weight: 780;
        }


        .dashboard-card-description {

            margin-top: 6px;

            color: #71888C;

            font-size: 12px;

            line-height: 1.6;
        }


        /* =========================================================
           ROADMAP PROGRESS
        ========================================================= */

        .dashboard-progress-track {

            height: 8px;

            margin-top: 24px;

            border-radius: 999px;

            overflow: hidden;

            background:
                rgba(255,255,255,0.055);
        }


        .dashboard-progress-fill {

            height: 100%;

            border-radius: 999px;

            background:
                linear-gradient(
                    90deg,
                    #087B84,
                    #12AAB3,
                    #9ED33C
                );

            box-shadow:
                0 0 18px
                rgba(18,170,179,0.22);
        }


        .dashboard-progress-meta {

            display: flex;

            justify-content: space-between;

            margin-top: 9px;

            color: #5D7478;

            font-size: 10px;
        }


        /* =========================================================
           FOCUS CARD
        ========================================================= */

        .dashboard-focus {

            padding: 20px;

            border-radius: 15px;

            background:
                rgba(18,170,179,0.045);

            border:
                1px solid
                rgba(18,170,179,0.12);
        }


        .dashboard-focus-label {

            color: #12AAB3;

            font-size: 9px;

            font-weight: 800;

            letter-spacing: 1.4px;

            text-transform: uppercase;
        }


        .dashboard-focus-title {

            margin-top: 8px;

            color: #EAF2F1;

            font-size: 16px;

            font-weight: 750;
        }


        .dashboard-focus-text {

            margin-top: 6px;

            color: #71888C;

            font-size: 12px;

            line-height: 1.6;
        }


        /* =========================================================
           PLATFORM ROW
        ========================================================= */

        .platform-row {

            display: flex;

            align-items: center;

            justify-content: space-between;

            padding:
                14px 0;

            border-bottom:
                1px solid
                rgba(255,255,255,0.045);
        }


        .platform-row:last-child {
            border-bottom: none;
        }


        .platform-name {

            color: #DCE8E7;

            font-size: 12px;

            font-weight: 650;
        }


        .platform-status {

            padding:
                5px 8px;

            border-radius: 999px;

            color: #657C80;

            background:
                rgba(255,255,255,0.035);

            border:
                1px solid
                rgba(255,255,255,0.05);

            font-size: 9px;

            font-weight: 650;
        }


        /* =========================================================
           CONTENT BUTTONS
        ========================================================= */

        .st-key-dashboard-content
        div[data-testid="stButton"] button {

            min-height: 42px !important;

            border-radius: 11px !important;

            border:
                1px solid
                rgba(18,170,179,0.18) !important;

            background:
                rgba(18,170,179,0.055) !important;

            color: #B9DCDD !important;

            font-size: 12px !important;

            font-weight: 700 !important;

            box-shadow: none !important;
        }


        .st-key-dashboard-content
        div[data-testid="stButton"] button:hover {

            background:
                rgba(18,170,179,0.11) !important;

            border-color:
                rgba(18,170,179,0.32) !important;

            color: #F4F7F5 !important;
        }


        /* =========================================================
           MOBILE
        ========================================================= */

        @media (max-width: 900px) {

            .st-key-dashboard-sidebar {

                position: relative;

                top: 0;

                min-height: auto;

                margin-bottom: 20px;
            }


            .dashboard-welcome h1 {

                font-size: 34px;
            }
        }


        </style>
        """
    )