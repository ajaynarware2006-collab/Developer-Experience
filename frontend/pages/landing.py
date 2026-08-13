import streamlit as st


def render_landing():

    # ==========================================
    # HERO
    # ==========================================

    st.html(
        """
        <section class="devxp-hero">

            <div class="devxp-eyebrow">
                AI-POWERED DEVELOPER GROWTH PLATFORM
            </div>


            <h1>
                Your developer journey.
                <br>
                <span>Understood.</span>
            </h1>


            <div class="devxp-hero-description">

                Connect your developer identity, understand
                where you stand, discover what you should learn
                next, and build a personalized path toward
                your career goals.

            </div>

        </section>
        """
    )


    # ==========================================
    # CTA BUTTONS
    # ==========================================
    st.html(
        """
        <div class="devxp-cta-row"></div>
        """
    )

    col1, col2, col3 , col4 = st.columns([1.3, 1, 1, 1.3])

    with col2:

        if st.button(
            "Get Started",
            type="primary",
            use_container_width=True,
            key="landing_get_started",
        ):
            st.session_state["page"] = "signup"
            st.rerun()


    with col3:

        if st.button(
            "Sign In",
            use_container_width=True,
            key="landing_signin",
        ):
            st.session_state["page"] = "login"
            st.rerun()


    # ==========================================
    # FEATURES
    # ==========================================

    st.html(
        """
        <section class="devxp-features">

            <article class="devxp-feature">

                <div class="devxp-feature-icon">
                    ◈
                </div>

                <div class="devxp-feature-title">
                    Know Your Developer Profile
                </div>

                <div class="devxp-feature-text">
                    Connect your GitHub, LeetCode, LinkedIn
                    and other developer platforms to build
                    a unified developer profile.
                </div>

            </article>


            <article class="devxp-feature">

                <div class="devxp-feature-icon">
                    ⌁
                </div>

                <div class="devxp-feature-title">
                    Get Your Personal Roadmap
                </div>

                <div class="devxp-feature-text">
                    Tell DEV/XP where you want to go and get
                    an AI-generated roadmap based on your
                    current skills and goals.
                </div>

            </article>


            <article class="devxp-feature">

                <div class="devxp-feature-icon">
                    ✦
                </div>

                <div class="devxp-feature-title">
                    Keep Growing
                </div>

                <div class="devxp-feature-text">
                    Track learning, projects and progress
                    while an AI assistant helps you decide
                    what to do next.
                </div>

            </article>

        </section>
        """
    )


    # ==========================================
    # PLATFORMS
    # ==========================================

    st.html(
        """
        <section class="devxp-platform-section">

            <div class="devxp-platform-label">
                Built around your developer identity
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