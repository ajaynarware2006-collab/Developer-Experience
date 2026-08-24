import streamlit as st


def load_feature_theme():
    st.html(
        """
        <style>       
        .features-page {
            width: min(1120px, 94%);
            margin: 0 auto;
            padding: 70px 0 40px;
        }


        /* ================================
        HERO
        ================================ */

        .features-hero {
            max-width: 780px;
            margin: 0 auto 70px;
            text-align: center;
        }

        .features-eyebrow {
            margin-bottom: 20px;

            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.22em;

            color: #78d6d0;
        }

        .features-hero h1 {
            margin: 0;

            color: #f4f7f5;

            font-size: clamp(
                42px,
                6vw,
                72px
            );

            line-height: 1.02;
            letter-spacing: -0.045em;
            font-weight: 800;
        }

        .features-hero h1 span {
            display: block;

            color: #78d6d0;
        }

        .features-hero p {
            max-width: 650px;
            margin: 28px auto 0;

            color: #91a5aa;

            font-size: 17px;
            line-height: 1.7;
        }


        /* ================================
        FEATURE GRID
        ================================ */

        .features-grid {
            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 18px;
        }

        .feature-card {
            position: relative;

            min-height: 270px;

            padding: 30px;

            border: 1px solid
                rgba(120, 214, 208, 0.10);

            border-radius: 20px;

            background:
                linear-gradient(
                    145deg,
                    rgba(255, 255, 255, 0.055),
                    rgba(255, 255, 255, 0.018)
                );

            backdrop-filter: blur(16px);
            -webkit-backdrop-filter: blur(16px);

            overflow: hidden;

            transition:
                transform 0.25s ease,
                border-color 0.25s ease,
                background 0.25s ease;
        }

        .feature-card::before {
            content: "";

            position: absolute;

            width: 150px;
            height: 150px;

            top: -90px;
            right: -80px;

            border-radius: 50%;

            background: rgba(
                120,
                214,
                208,
                0.08
            );

            filter: blur(30px);
        }

        .feature-card:hover {
            transform: translateY(-6px);

            border-color:
                rgba(120, 214, 208, 0.30);

            background:
                linear-gradient(
                    145deg,
                    rgba(255, 255, 255, 0.075),
                    rgba(255, 255, 255, 0.025)
                );
        }

        .feature-number {
            position: absolute;

            top: 25px;
            right: 27px;

            color: rgba(
                145,
                165,
                170,
                0.35
            );

            font-size: 12px;
            font-weight: 700;
            letter-spacing: 0.1em;
        }

        .feature-icon {
            display: flex;

            width: 48px;
            height: 48px;

            align-items: center;
            justify-content: center;

            margin-bottom: 28px;

            border: 1px solid
                rgba(120, 214, 208, 0.18);

            border-radius: 14px;

            background:
                rgba(120, 214, 208, 0.07);

            color: #78d6d0;

            font-size: 22px;
        }

        .feature-card h2 {
            margin: 0 0 12px;

            color: #f4f7f5;

            font-size: 20px;
            font-weight: 700;
        }

        .feature-card p {
            margin: 0;

            color: #84999e;

            font-size: 14px;
            line-height: 1.7;
        }


        /* ================================
        BOTTOM SECTION
        ================================ */

        .features-bottom {
            display: flex;

            align-items: center;
            justify-content: space-between;

            gap: 40px;

            margin-top: 18px;
            padding: 45px 40px;

            border: 1px solid
                rgba(120, 214, 208, 0.10);

            border-radius: 20px;

            background:
                rgba(255, 255, 255, 0.025);
        }

        .features-bottom-label {
            margin-bottom: 10px;

            color: #78d6d0;

            font-size: 11px;
            font-weight: 700;
            letter-spacing: 0.18em;
        }

        .features-bottom h2 {
            margin: 0 0 10px;

            color: #f4f7f5;

            font-size: 30px;
        }

        .features-bottom p {
            max-width: 650px;

            margin: 0;

            color: #84999e;

            line-height: 1.7;
        }

        .features-stat {
            display: flex;

            flex-direction: column;

            align-items: center;

            min-width: 130px;
        }

        .features-stat span {
            color: #78d6d0;

            font-size: 64px;
            font-weight: 800;

            line-height: 1;
        }

        .features-stat small {
            margin-top: 10px;

            color: #687d82;

            font-size: 10px;
            font-weight: 700;

            letter-spacing: 0.16em;
        }


        /* ================================
        CTA
        ================================ */

        .features-cta {
            width: min(1120px, 94%);

            margin: 18px auto 70px;
            padding: 32px;

            border: 1px solid
                rgba(120, 214, 208, 0.10);

            border-radius: 20px;

            background:
                linear-gradient(
                    100deg,
                    rgba(120, 214, 208, 0.08),
                    rgba(255, 255, 255, 0.025)
                );

            display: flex;
            align-items: center;
            justify-content: space-between;
        }

        .features-cta span {
            color: #78d6d0;

            font-size: 10px;
            font-weight: 700;

            letter-spacing: 0.18em;
        }

        .features-cta h2 {
            margin: 8px 0 0;

            color: #f4f7f5;

            font-size: 24px;
        }

        .st-key-feature-button button{
            border : none;
        }


        /* ================================
        RESPONSIVE
        ================================ */

        @media (max-width: 900px) {

            .features-grid {
                grid-template-columns:
                    repeat(2, 1fr);
            }

        }


        @media (max-width: 650px) {

            .features-page {
                padding-top: 45px;
            }

            .features-grid {
                grid-template-columns: 1fr;
            }

            .features-bottom {
                flex-direction: column;
                align-items: flex-start;

                padding: 32px 25px;
            }

            .features-stat {
                align-items: flex-start;
            }

            .features-cta {
                padding: 28px 24px;
            }

        }
        </style>
        """
    )
