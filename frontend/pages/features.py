import streamlit as st
from frontend.styles.feature_theme import load_feature_theme

def render_features():

    load_feature_theme()

    st.html(
        """
        <div class="features-page">

            <div class="features-hero">

                <div class="features-eyebrow">
                    DEV/XP · FEATURES
                </div>

                <h1>
                    Everything you need to
                    <span>level up as a developer.</span>
                </h1>

                <p>
                    DEV/XP turns your developer goals into a
                    structured journey — from your first profile
                    to measurable progress.
                </p>

            </div>


            <div class="features-grid">

                <div class="feature-card">

                    <div class="feature-number">
                        01
                    </div>

                    <div class="feature-icon">
                        ◈
                    </div>

                    <h2>
                        Developer Profile
                    </h2>

                    <p>
                        Build your developer identity with your
                        career goal, experience, skills, target,
                        timeline and available study time.
                    </p>

                </div>


                <div class="feature-card">

                    <div class="feature-number">
                        02
                    </div>

                    <div class="feature-icon">
                        ◎
                    </div>

                    <h2>
                        Personalized Roadmap
                    </h2>

                    <p>
                        Turn your career goal and current skill
                        level into a structured roadmap designed
                        around your developer journey.
                    </p>

                </div>


                <div class="feature-card">

                    <div class="feature-number">
                        03
                    </div>

                    <div class="feature-icon">
                        ◫
                    </div>

                    <h2>
                        Learning Tasks
                    </h2>

                    <p>
                        Break your roadmap into practical,
                        actionable learning tasks so you always
                        know what to work on next.
                    </p>

                </div>


                <div class="feature-card">

                    <div class="feature-number">
                        04
                    </div>

                    <div class="feature-icon">
                        ↗
                    </div>

                    <h2>
                        Progress Tracking
                    </h2>

                    <p>
                        Track completed work and see your
                        development journey move forward instead
                        of relying on guesswork.
                    </p>

                </div>


                <div class="feature-card">

                    <div class="feature-number">
                        05
                    </div>

                    <div class="feature-icon">
                        ⌘
                    </div>

                    <h2>
                        Developer Dashboard
                    </h2>

                    <p>
                        Keep your profile, roadmap, goals and
                        progress together in one focused
                        developer workspace.
                    </p>

                </div>


                <div class="feature-card">

                    <div class="feature-number">
                        06
                    </div>

                    <div class="feature-icon">
                        ✓
                    </div>

                    <h2>
                        Secure Authentication
                    </h2>

                    <p>
                        Protect your account with secure
                        authentication and email ownership
                        verification.
                    </p>

                </div>

            </div>


            <div class="features-bottom">

                <div>

                    <div class="features-bottom-label">
                        BUILT TO GROW
                    </div>

                    <h2>
                        More than a roadmap.
                    </h2>

                    <p>
                        DEV/XP is being built as a complete
                        developer growth system — with more
                        capabilities coming as the platform evolves.
                    </p>

                </div>

                <div class="features-stat">

                    <span>
                        06
                    </span>

                    <small>
                        CORE FEATURES
                    </small>

                </div>

            </div>

        </div>
        """
    )

    st.html(
        """
        <div class="features-cta">

            <div>

                <span>
                    READY TO START?
                </span>

                <h2>
                    Build your developer journey.
                </h2>

            </div>

        </div>
        """
    )

    if st.button(
        "Create your DEV/XP account →",
        type="primary",
        use_container_width=True,
        key="features_signup",
    ):

        st.session_state["page"] = "signup"

        st.rerun()