import streamlit as st


def render_landing():

    # ============================================================
    # HERO
    # ============================================================

    st.html(
        """
        <section class="devxp-hero">

            <div class="devxp-eyebrow">
                ⚡ AI-POWERED DEVELOPER GROWTH PLATFORM
            </div>

            <h1>
                Build your career.
                <br>
                <span>Understand your path.</span>
            </h1>

            <div class="devxp-hero-description">

                DEV/XP connects your developer identity,
                understands your current skills, and creates
                a personalized roadmap for where you want to go.

            </div>

        </section>
        """
    )


    # ============================================================
    # CTA BUTTONS
    # ============================================================

    st.html(
        """
        <div class="devxp-cta-row"></div>
        """
    )

    col1, col2, col3, col4 = st.columns(
        [1.4, 1, 1, 1.4]
    )


    # ------------------------------------------------------------
    # GET STARTED
    # ------------------------------------------------------------

    with col2:

        if st.button(
            "Get Started",
            type="primary",
            use_container_width=True,
            key="landing_get_started",
        ):

            st.session_state["page"] = "signup"

            st.rerun()


    # ------------------------------------------------------------
    # SIGN IN
    # ------------------------------------------------------------

    with col3:

        if st.button(
            "Sign In",
            use_container_width=True,
            key="landing_signin",
        ):

            st.session_state["page"] = "login"

            st.rerun()


    # ============================================================
    # FEATURE INTRO
    # ============================================================

    st.html(
        """
        <div
            style="
                text-align:center;
                margin:100px auto 35px;
                max-width:650px;
            "
        >

            <div
                style="
                    color:#12AAB3;
                    font-size:11px;
                    font-weight:750;
                    letter-spacing:2px;
                    text-transform:uppercase;
                    margin-bottom:12px;
                "
            >
                ONE PLACE FOR YOUR DEVELOPER JOURNEY
            </div>

            <div
                style="
                    color:#F4F7F5;
                    font-size:30px;
                    font-weight:800;
                    letter-spacing:-1px;
                "
            >
                Understand where you are.
                <br>
                Know where to go next.
            </div>

        </div>
        """
    )


    # ============================================================
    # FEATURE CARDS
    # ============================================================

    st.html(
        """
        <section class="devxp-features">


            <!-- CARD 1 -->

            <article class="devxp-feature">

                <div class="devxp-feature-icon">
                    ◈
                </div>

                <div class="devxp-feature-title">
                    Your Developer Profile
                </div>

                <div class="devxp-feature-text">

                    Connect GitHub, LeetCode, LinkedIn
                    and other platforms to create a unified
                    view of your developer identity.

                </div>

            </article>


            <!-- CARD 2 -->

            <article class="devxp-feature">

                <div class="devxp-feature-icon">
                    ⌁
                </div>

                <div class="devxp-feature-title">
                    AI-Powered Roadmap
                </div>

                <div class="devxp-feature-text">

                    Tell DEV/XP your career goal and let AI
                    generate a personalized learning path
                    based on your current skills.

                </div>

            </article>


            <!-- CARD 3 -->

            <article class="devxp-feature">

                <div class="devxp-feature-icon">
                    ✦
                </div>

                <div class="devxp-feature-title">
                    Continuous Growth
                </div>

                <div class="devxp-feature-text">

                    Track your skills, projects and learning
                    progress while DEV/XP continuously helps
                    you decide what to focus on next.

                </div>

            </article>


        </section>
        """
    )


    # ============================================================
    # PLATFORM SECTION
    # ============================================================

    st.html(
        """
        <section class="devxp-platform-section">

            <div class="devxp-platform-label">
                YOUR DEVELOPER ECOSYSTEM
            </div>


            <div class="devxp-platform-list">

                <span>GitHub</span>

                <span>LeetCode</span>

                <span>LinkedIn</span>

                <span>Kaggle</span>

                <span>HackerRank</span>

            </div>

        </section>
        """
    )