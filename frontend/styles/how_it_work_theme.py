import streamlit as st


def load_how_it_works_theme():

    # ============================================================
    # PAGE CSS
    # ============================================================

    st.html(
        """
        <style>

        /* ========================================================
           PAGE
        ======================================================== */

        .how-page {
            width: min(1050px, 94%);
            margin: 0 auto;
            padding: 70px 0 80px;
        }


        /* ========================================================
           HERO
        ======================================================== */

        .how-hero {
            max-width: 800px;
            margin: 0 auto 90px;
            text-align: center;
        }

        .how-eyebrow {
            margin-bottom: 18px;

            color: #78d6d0;

            font-size: 11px;
            font-weight: 700;

            letter-spacing: 0.22em;
        }

        .how-hero h1 {
            margin: 0;

            color: #f4f7f5;

            font-size: clamp(
                42px,
                6vw,
                70px
            );

            line-height: 1.02;
            letter-spacing: -0.045em;

            font-weight: 800;
        }

        .how-hero h1 span {
            display: block;
            color: #78d6d0;
        }

        .how-hero p {
            max-width: 650px;

            margin: 28px auto 0;

            color: #91a5aa;

            font-size: 17px;
            line-height: 1.7;
        }


        /* ========================================================
           JOURNEY
        ======================================================== */

        .journey {
            position: relative;

            max-width: 850px;

            margin: 0 auto;
        }

        .journey-line {
            position: absolute;

            left: 34px;
            top: 35px;
            bottom: 35px;

            width: 1px;

            background:
                linear-gradient(
                    to bottom,
                    rgba(120, 214, 208, 0),
                    rgba(120, 214, 208, 0.28),
                    rgba(120, 214, 208, 0)
                );
        }

        .journey-step {
            position: relative;

            display: grid;

            grid-template-columns:
                70px 1fr;

            gap: 30px;

            margin-bottom: 70px;
        }

        .journey-step:last-child {
            margin-bottom: 0;
        }


        /* ========================================================
           STEP MARKER
        ======================================================== */

        .step-marker {
            position: relative;

            z-index: 2;

            display: flex;

            width: 70px;
            height: 70px;

            align-items: center;
            justify-content: center;

            border: 1px solid
                rgba(120, 214, 208, 0.25);

            border-radius: 50%;

            background: #10191c;

            box-shadow:
                0 0 0 8px
                rgba(120, 214, 208, 0.025);
        }

        .step-marker span {
            color: #78d6d0;

            font-size: 12px;
            font-weight: 800;

            letter-spacing: 0.08em;
        }


        /* ========================================================
           STEP CONTENT
        ======================================================== */

        .step-content {
            padding: 8px 30px 30px;

            border-bottom: 1px solid
                rgba(255, 255, 255, 0.055);
        }

        .journey-step:last-child .step-content {
            border-bottom: none;
        }

        .step-label {
            margin-bottom: 10px;

            color: #687d82;

            font-size: 10px;
            font-weight: 700;

            letter-spacing: 0.18em;
        }

        .step-content h2 {
            margin: 0 0 14px;

            color: #f4f7f5;

            font-size: 28px;
            font-weight: 750;

            letter-spacing: -0.02em;
        }

        .step-content p {
            max-width: 650px;

            margin: 0;

            color: #84999e;

            font-size: 15px;
            line-height: 1.75;
        }


        /* ========================================================
           STEP DETAILS
        ======================================================== */

        .step-detail {
            display: flex;

            flex-wrap: wrap;

            gap: 8px;

            margin-top: 22px;
        }

        .step-detail span {
            padding: 7px 11px;

            border: 1px solid
                rgba(120, 214, 208, 0.12);

            border-radius: 8px;

            background:
                rgba(120, 214, 208, 0.035);

            color: #78d6d0;

            font-size: 9px;
            font-weight: 700;

            letter-spacing: 0.12em;
        }


        /* ========================================================
           CORE LOOP
        ======================================================== */

        .core-loop {
            margin-top: 120px;
            padding: 55px 40px;

            border: 1px solid
                rgba(120, 214, 208, 0.10);

            border-radius: 22px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255, 255, 255, 0.045),
                    rgba(255, 255, 255, 0.015)
                );
        }

        .loop-heading {
            margin-bottom: 45px;

            text-align: center;
        }

        .loop-heading h2 {
            margin: 0;

            color: #f4f7f5;

            font-size: 36px;
            line-height: 1.1;

            letter-spacing: -0.035em;
        }

        .loop-heading h2 span {
            color: #78d6d0;
        }


        /* ========================================================
           LOOP GRID
        ======================================================== */

        .loop-grid {
            display: grid;

            grid-template-columns:
                1fr auto 1fr auto 1fr auto 1fr;

            align-items: center;

            gap: 18px;
        }

        .loop-card {
            min-width: 0;

            text-align: center;
        }

        .loop-icon {
            display: flex;

            width: 50px;
            height: 50px;

            margin: 0 auto 16px;

            align-items: center;
            justify-content: center;

            border: 1px solid
                rgba(120, 214, 208, 0.18);

            border-radius: 14px;

            background:
                rgba(120, 214, 208, 0.06);

            color: #78d6d0;

            font-size: 20px;
        }

        .loop-card h3 {
            margin: 0 0 7px;

            color: #f4f7f5;

            font-size: 16px;
        }

        .loop-card p {
            margin: 0;

            color: #74898e;

            font-size: 12px;
            line-height: 1.5;
        }

        .loop-arrow {
            color: rgba(
                120,
                214,
                208,
                0.45
            );

            font-size: 20px;
        }


        /* ========================================================
           CTA
        ======================================================== */

        .how-cta {
            margin-top: 22px;
            padding: 50px 40px;

            border: 1px solid
                rgba(120, 214, 208, 0.10);

            border-radius: 22px;

            background:
                linear-gradient(
                    100deg,
                    rgba(120, 214, 208, 0.08),
                    rgba(255, 255, 255, 0.025)
                );

            text-align: center;
        }

        .how-cta h2 {
            margin: 0;

            color: #f4f7f5;

            font-size: 30px;

            letter-spacing: -0.025em;
        }

        .how-cta p {
            margin: 12px 0 0;

            color: #84999e;

            font-size: 15px;
        }


        /* ========================================================
           RESPONSIVE
        ======================================================== */

        @media (max-width: 850px) {

            .loop-grid {
                grid-template-columns:
                    repeat(2, 1fr);
            }

            .loop-arrow {
                display: none;
            }

        }


        @media (max-width: 650px) {

            .how-page {
                padding-top: 45px;
            }

            .journey-step {
                grid-template-columns:
                    50px 1fr;

                gap: 18px;
            }

            .step-marker {
                width: 50px;
                height: 50px;
            }

            .journey-line {
                left: 24px;
            }

            .step-content {
                padding-left: 0;
                padding-right: 0;
            }

            .step-content h2 {
                font-size: 23px;
            }

            .core-loop {
                padding: 40px 22px;
            }

            .loop-grid {
                grid-template-columns: 1fr;
                gap: 30px;
            }

            .how-cta {
                padding: 40px 24px;
            }

        }

        </style>
        """,
    )