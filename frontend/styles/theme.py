import streamlit as st


def load_theme():
    st.html(
        """
        <style>

        /* =========================================================
           DEV/XP — DARK GLASS THEME
           Palette:
           Background : #081316
           Surface    : #142022
           Teal       : #087B84
           Aqua       : #12AAB3
           Lime       : #9ED33C
           Coral      : #EF6843
        ========================================================= */


        /* =========================================================
           GLOBAL APP
        ========================================================= */

        .stApp {
            min-height: 100vh;

            background:
                radial-gradient(
                    circle at 8% 8%,
                    rgba(18, 170, 179, 0.12),
                    transparent 30%
                ),

                radial-gradient(
                    circle at 92% 18%,
                    rgba(239, 104, 67, 0.08),
                    transparent 28%
                ),

                radial-gradient(
                    circle at 50% 100%,
                    rgba(50, 150, 180, 0.08),
                    transparent 35%
                ),

                #081316;

            color: #F4F7F5;
        }


        /* =========================================================
           STREAMLIT UI CLEANUP
        ========================================================= */

        #MainMenu {
            visibility: hidden;
        }

        header {
            visibility: hidden;
        }

        footer {
            visibility: hidden;
        }

        [data-testid="stToolbar"] {
            visibility: hidden;
        }

        .block-container {
            max-width: 1400px;

            padding-top: 0.5rem;
            padding-bottom: 80px;
        }


        /* =========================================================
           SCROLLBAR
        ========================================================= */

        ::-webkit-scrollbar {
            width: 8px;
        }

        ::-webkit-scrollbar-track {
            background: #081316;
        }

        ::-webkit-scrollbar-thumb {
            background: #23474B;
            border-radius: 20px;
        }

        ::-webkit-scrollbar-thumb:hover {
            background: #087B84;
        }


        /* =========================================================
           NAVBAR
        ========================================================= */

        .devxp-navbar {
            width: 100%;
            height: 78px;

            display: flex;

            align-items: center;
            justify-content: space-between;

            border-bottom:
                1px solid
                rgba(255, 255, 255, 0.07);
        }


        .devxp-brand {
            display: flex;

            align-items: center;

            gap: 11px;

            color: #F4F7F5;

            font-size: 22px;

            font-weight: 850;

            letter-spacing: -0.7px;
        }


        .devxp-brand-mark {
            width: 38px;
            height: 38px;

            display: flex;

            align-items: center;
            justify-content: center;

            border-radius: 11px;

            background:
                linear-gradient(
                    135deg,
                    #087B84,
                    #12AAB3
                );

            color: #FFFFFF;

            font-size: 15px;

            font-weight: 900;

            box-shadow:
                0 8px 25px
                rgba(18, 170, 179, 0.22);
        }


        .devxp-brand span {
            color: #9ED33C;
        }


        .devxp-nav-right {
            display: flex;

            align-items: center;

            gap: 34px;
        }


        .devxp-nav-link {
            color: #91A5AA;

            font-size: 14px;

            font-weight: 550;

            transition:
                color 0.2s ease;
        }


        .devxp-nav-link:hover {
            color: #12AAB3;
        }


        /* =========================================================
           HERO
        ========================================================= */

        .devxp-hero {
            min-height: 650px;

            display: flex;

            flex-direction: column;

            align-items: center;

            justify-content: center;

            padding:
                80px 20px 55px;

            text-align: center;
        }


        .devxp-eyebrow {
            display: inline-flex;

            align-items: center;

            padding:
                8px 16px;

            border:
                1px solid
                rgba(158, 211, 60, 0.28);

            border-radius: 999px;

            background:
                rgba(158, 211, 60, 0.06);

            color: #9ED33C;

            font-size: 11px;

            font-weight: 750;

            letter-spacing: 1.3px;
        }


        .devxp-hero h1 {
            max-width: 950px;

            margin:
                28px 0 0;

            color: #F4F7F5;

            font-size:
                clamp(48px, 7vw, 86px);

            line-height: 0.98;

            font-weight: 850;

            letter-spacing: -4px;
        }


        .devxp-hero h1 span {
            color: #9ED33C;

            text-shadow:
                0 0 30px
                rgba(158, 211, 60, 0.12);
        }


        .devxp-hero-description {
            max-width: 700px;

            margin-top: 30px;

            color: #91A5AA;

            font-size: 17px;

            line-height: 1.7;
        }


        /* =========================================================
           CTA AREA
        ========================================================= */

        .devxp-cta-row {
            width: 100%;

            max-width: 520px;

            margin:
                30px auto 0;
        }


        /* =========================================================
           ALL STREAMLIT BUTTONS
        ========================================================= */

        div.stButton > button {
            min-height: 46px;

            border-radius: 10px;

            border:
                1px solid
                rgba(255, 255, 255, 0.10);

            background:
                rgba(255, 255, 255, 0.035);

            color: #EAF2F1;

            font-weight: 700;

            transition:
                transform 0.2s ease,
                box-shadow 0.2s ease,
                border-color 0.2s ease,
                background 0.2s ease;
        }


        div.stButton > button:hover {
            transform:
                translateY(-2px);

            border-color:
                rgba(18, 170, 179, 0.45);

            background:
                rgba(18, 170, 179, 0.08);

            color: #FFFFFF;

            box-shadow:
                0 10px 30px
                rgba(0, 0, 0, 0.25);
        }


        /* =========================================================
           PRIMARY BUTTON
        ========================================================= */

        div.stButton > button[kind="primary"] {
            background:
                linear-gradient(
                    135deg,
                    #087B84,
                    #12AAB3
                );

            border:
                1px solid
                #12AAB3;

            color: #FFFFFF;

            box-shadow:
                0 0 0 1px
                rgba(18, 170, 179, 0.10),

                0 10px 30px
                rgba(18, 170, 179, 0.18);
        }


        div.stButton > button[kind="primary"]:hover {
            background:
                linear-gradient(
                    135deg,
                    #096C74,
                    #10BEC8
                );

            color: #FFFFFF;

            box-shadow:
                0 0 25px
                rgba(18, 170, 179, 0.25),

                0 15px 40px
                rgba(18, 170, 179, 0.20);
        }


        /* =========================================================
           FEATURE CARDS
        ========================================================= */

        .devxp-features {
            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 18px;

            max-width: 1100px;

            margin: 0 auto;
        }


        .devxp-feature {
            min-height: 200px;

            padding: 28px;

            border:
                1px solid
                rgba(255, 255, 255, 0.08);

            border-radius: 18px;

            background:
                rgba(20, 32, 34, 0.62);

            backdrop-filter:
                blur(18px);

            -webkit-backdrop-filter:
                blur(18px);

            box-shadow:
                0 20px 50px
                rgba(0, 0, 0, 0.25),

                inset 0 1px 0
                rgba(255, 255, 255, 0.04);

            transition:
                transform 0.25s ease,
                box-shadow 0.25s ease,
                border-color 0.25s ease;
        }


        .devxp-feature:hover {
            transform:
                translateY(-6px);

            border-color:
                rgba(18, 170, 179, 0.25);

            box-shadow:
                0 25px 60px
                rgba(0, 0, 0, 0.35),

                0 0 30px
                rgba(18, 170, 179, 0.05);
        }


        .devxp-feature-icon {
            width: 44px;
            height: 44px;

            display: flex;

            align-items: center;
            justify-content: center;

            margin-bottom: 20px;

            border-radius: 12px;

            background:
                rgba(18, 170, 179, 0.10);

            color: #12AAB3;

            font-size: 18px;

            box-shadow:
                inset 0 0 20px
                rgba(18, 170, 179, 0.04);
        }


        .devxp-feature:nth-child(2)
        .devxp-feature-icon {
            background:
                rgba(158, 211, 60, 0.09);

            color: #9ED33C;
        }


        .devxp-feature:nth-child(3)
        .devxp-feature-icon {
            background:
                rgba(239, 104, 67, 0.09);

            color: #EF6843;
        }


        .devxp-feature-title {
            margin-bottom: 10px;

            color: #F0F6F4;

            font-size: 16px;

            font-weight: 750;
        }


        .devxp-feature-text {
            color: #91A5AA;

            font-size: 13px;

            line-height: 1.7;
        }


        /* =========================================================
           PLATFORM SECTION
        ========================================================= */

        .devxp-platform-section {
            max-width: 1100px;

            margin:
                90px auto 0;

            padding-top: 35px;

            border-top:
                1px solid
                rgba(255, 255, 255, 0.07);

            text-align: center;
        }


        .devxp-platform-label {
            margin-bottom: 25px;

            color: #6F858A;

            font-size: 11px;

            font-weight: 750;

            letter-spacing: 2px;

            text-transform: uppercase;
        }


        .devxp-platform-list {
            display: flex;

            align-items: center;

            justify-content: center;

            gap: 55px;

            color: #91A5AA;

            font-size: 14px;

            font-weight: 650;
        }


        .devxp-platform-list span {
            transition:
                color 0.2s ease;
        }


        .devxp-platform-list span:hover {
            color: #12AAB3;
        }


        /* =========================================================
           GLASS AUTH CARD
        ========================================================= */

        .st-key-auth-card {
            position: relative;

            width: 100%;

            margin:
                60px auto 50px;

            padding:
                42px 46px 38px;

            border-radius: 24px;

            background:
                rgba(20, 32, 34, 0.65);

            border:
                1px solid
                rgba(255, 255, 255, 0.10);

            backdrop-filter:
                blur(24px)
                saturate(120%);

            -webkit-backdrop-filter:
                blur(24px)
                saturate(120%);

            box-shadow:
                0 30px 80px
                rgba(0, 0, 0, 0.40),

                0 8px 25px
                rgba(0, 0, 0, 0.25),

                inset 0 1px 0
                rgba(255, 255, 255, 0.06);

            overflow: hidden;
        }


        /* Top glass reflection */

        .st-key-auth-card::before {
            content: "";

            position: absolute;

            top: 0;
            left: 0;
            right: 0;

            height: 2px;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    rgba(18, 170, 179, 0.55),
                    transparent
                );

            pointer-events: none;
        }


        /* Background glow */

        .st-key-auth-card::after {
            content: "";

            position: absolute;

            width: 330px;
            height: 330px;

            top: -200px;
            right: -120px;

            border-radius: 50%;

            background:
                rgba(18, 170, 179, 0.12);

            filter:
                blur(80px);

            pointer-events: none;
        }


        /* =========================================================
           AUTH HEADER
        ========================================================= */

        .auth-card-header {
            position: relative;

            z-index: 2;

            padding:
                0 5px 26px;

            text-align: center;
        }


        .auth-title {
            color: #F4F7F5;

            font-size: 36px;

            font-weight: 850;

            letter-spacing: -1.3px;

            line-height: 1.1;
        }


        .auth-subtitle {
            max-width: 390px;

            margin:
                13px auto 0;

            color: #91A5AA;

            font-size: 14px;

            line-height: 1.6;
        }


        /* =========================================================
           AUTH INPUTS
        ========================================================= */

        .st-key-auth-card input {
            background:
                rgba(255, 255, 255, 0.055)
                !important;

            border:
                1px solid
                rgba(255, 255, 255, 0.10)
                !important;

            border-radius:
                10px
                !important;

            color:
                #F4F7F5
                !important;

            transition:
                border-color 0.2s ease,
                box-shadow 0.2s ease,
                background 0.2s ease;
        }


        .st-key-auth-card input:focus {
            border-color:
                rgba(18, 170, 179, 0.70)
                !important;

            background:
                rgba(255, 255, 255, 0.075)
                !important;

            box-shadow:
                0 0 0 3px
                rgba(18, 170, 179, 0.12)
                !important;
        }


        .st-key-auth-card input::placeholder {
            color:
                #687D82
                !important;
        }


        .st-key-auth-card label {
            color:
                #B9C7C8
                !important;

            font-size:
                13px
                !important;

            font-weight:
                650
                !important;
        }


        /* =========================================================
           AUTH PRIMARY BUTTON
        ========================================================= */

        .st-key-auth-card
        button[kind="primary"] {
            background:
                linear-gradient(
                    135deg,
                    #087B84,
                    #12AAB3
                );

            border:
                1px solid
                #12AAB3;

            color:
                #FFFFFF;

            box-shadow:
                0 0 0 1px
                rgba(18, 170, 179, 0.10),

                0 8px 25px
                rgba(18, 170, 179, 0.20);
        }


        .st-key-auth-card
        button[kind="primary"]:hover {
            transform:
                translateY(-2px);

            box-shadow:
                0 0 25px
                rgba(18, 170, 179, 0.25),

                0 14px 35px
                rgba(18, 170, 179, 0.20);
        }


        /* =========================================================
           AUTH SECONDARY BUTTON
        ========================================================= */

        .st-key-auth-card
        button:not([kind="primary"]) {
            background:
                rgba(255, 255, 255, 0.035);

            color:
                #B9C7C8;

            border:
                1px solid
                rgba(255, 255, 255, 0.10);
        }


        .st-key-auth-card
        button:not([kind="primary"]):hover {
            background:
                rgba(18, 170, 179, 0.07);

            color:
                #FFFFFF;

            border-color:
                rgba(18, 170, 179, 0.30);
        }


        /* =========================================================
           AUTH SWITCH
        ========================================================= */

        .auth-switch-label {
            position: relative;

            z-index: 2;

            margin:
                20px 0 8px;

            text-align: center;

            color: #71878C;

            font-size: 13px;
        }


        /* =========================================================
           ALERTS
        ========================================================= */

        .st-key-auth-card
        [data-testid="stAlert"] {
            border-radius: 10px;

            background:
                rgba(255, 255, 255, 0.04);

            border:
                1px solid
                rgba(255, 255, 255, 0.08);

            backdrop-filter:
                blur(10px);
        }


        /* =========================================================
           DIVIDERS
        ========================================================= */

        hr {
            border-color:
                rgba(255, 255, 255, 0.07)
                !important;
        }


        /* =========================================================
           TEXT SELECTION
        ========================================================= */

        ::selection {
            background:
                rgba(18, 170, 179, 0.35);

            color:
                #FFFFFF;
        }


        /* =========================================================
           RESPONSIVE
        ========================================================= */

        @media (max-width: 800px) {

            .devxp-nav-right {
                display: none;
            }


            .devxp-hero {
                min-height: 560px;

                padding:
                    60px 15px;
            }


            .devxp-hero h1 {
                font-size: 48px;

                letter-spacing: -2px;
            }


            .devxp-hero-description {
                font-size: 15px;
            }


            .devxp-features {
                grid-template-columns:
                    1fr;
            }


            .devxp-platform-list {
                flex-wrap: wrap;

                gap: 20px;
            }


            .st-key-auth-card {
                padding:
                    32px 24px 30px;

                border-radius: 20px;
            }


            .auth-title {
                font-size: 30px;
            }
        }


        /* =========================================================
           VERY SMALL SCREENS
        ========================================================= */

        @media (max-width: 480px) {

            .devxp-hero h1 {
                font-size: 40px;

                letter-spacing: -1.5px;
            }


            .devxp-eyebrow {
                font-size: 9px;

                letter-spacing: 0.9px;
            }


            .devxp-feature {
                padding: 22px;
            }


            .st-key-auth-card {
                padding:
                    28px 18px;
            }
        }

        </style>
        """
    )