import streamlit as st
from pathlib import Path
from frontend.styles.how_it_work_theme import load_how_it_works_theme


def render_how_it_works():

    load_how_it_works_theme()

    st.html(
        """
        <div class="how-page">

            <!-- HERO -->

            <section class="how-hero">

                <div class="how-eyebrow">
                    DEV/XP · HOW IT WORKS
                </div>

                <h1>
                    Your developer journey,
                    <span>structured.</span>
                </h1>

                <p>
                    DEV/XP takes you from knowing where you want
                    to go to knowing exactly what you can work on
                    next.
                </p>

            </section>


            <!-- JOURNEY -->

            <section class="journey">

                <div class="journey-line"></div>


                <!-- STEP 01 -->

                <div class="journey-step">

                    <div class="step-marker">
                        <span>01</span>
                    </div>

                    <div class="step-content">

                        <div class="step-label">
                            START HERE
                        </div>

                        <h2>
                            Create your account
                        </h2>

                        <p>
                            Create your DEV/XP account with your
                            name, email and password. Your account
                            becomes the foundation of your developer
                            workspace.
                        </p>

                        <div class="step-detail">

                            <span>NAME</span>
                            <span>EMAIL</span>
                            <span>PASSWORD</span>

                        </div>

                    </div>

                </div>


                <!-- STEP 02 -->

                <div class="journey-step">

                    <div class="step-marker">
                        <span>02</span>
                    </div>

                    <div class="step-content">

                        <div class="step-label">
                            VERIFY
                        </div>

                        <h2>
                            Verify your email
                        </h2>

                        <p>
                            DEV/XP sends a verification code to
                            your email. Enter the code to prove
                            that you control the account you're
                            creating.
                        </p>

                        <div class="step-detail">

                            <span>OTP</span>
                            <span>EMAIL</span>
                            <span>VERIFIED</span>

                        </div>

                    </div>

                </div>


                <!-- STEP 03 -->

                <div class="journey-step">

                    <div class="step-marker">
                        <span>03</span>
                    </div>

                    <div class="step-content">

                        <div class="step-label">
                            DEFINE YOURSELF
                        </div>

                        <h2>
                            Build your developer profile
                        </h2>

                        <p>
                            Tell DEV/XP where you currently are
                            and where you want to go. Your skills,
                            experience, career goal, target and
                            timeline become your developer profile.
                        </p>

                        <div class="step-detail">

                            <span>SKILLS</span>
                            <span>EXPERIENCE</span>
                            <span>GOAL</span>
                            <span>TIMELINE</span>

                        </div>

                    </div>

                </div>


                <!-- STEP 04 -->

                <div class="journey-step">

                    <div class="step-marker">
                        <span>04</span>
                    </div>

                    <div class="step-content">

                        <div class="step-label">
                            GET DIRECTION
                        </div>

                        <h2>
                            Get your developer roadmap
                        </h2>

                        <p>
                            Your profile becomes the input for
                            your learning roadmap. DEV/XP organizes
                            your journey into phases and practical
                            learning tasks.
                        </p>

                        <div class="step-detail">

                            <span>PHASES</span>
                            <span>TASKS</span>
                            <span>PROJECTS</span>

                        </div>

                    </div>

                </div>


                <!-- STEP 05 -->

                <div class="journey-step">

                    <div class="step-marker">
                        <span>05</span>
                    </div>

                    <div class="step-content">

                        <div class="step-label">
                            TAKE ACTION
                        </div>

                        <h2>
                            Work through your tasks
                        </h2>

                        <p>
                            Instead of wondering what to learn
                            next, work through the tasks that make
                            up your roadmap and turn learning into
                            consistent action.
                        </p>

                        <div class="step-detail">

                            <span>LEARN</span>
                            <span>BUILD</span>
                            <span>PRACTICE</span>

                        </div>

                    </div>

                </div>


                <!-- STEP 06 -->

                <div class="journey-step">

                    <div class="step-marker">
                        <span>06</span>
                    </div>

                    <div class="step-content">

                        <div class="step-label">
                            KEEP MOVING
                        </div>

                        <h2>
                            Track your progress
                        </h2>

                        <p>
                            Your dashboard brings your developer
                            journey together so you can see what
                            you've completed, where you are and
                            what comes next.
                        </p>

                        <div class="step-detail">

                            <span>PROGRESS</span>
                            <span>ROADMAP</span>
                            <span>DASHBOARD</span>

                        </div>

                    </div>

                </div>

            </section>


            <!-- CORE LOOP -->

            <section class="core-loop">

                <div class="loop-heading">

                    <div class="how-eyebrow">
                        THE DEV/XP LOOP
                    </div>

                    <h2>
                        Know the goal.
                        <span>Do the work.</span>
                    </h2>

                </div>


                <div class="loop-grid">

                    <div class="loop-card">

                        <div class="loop-icon">
                            ◎
                        </div>

                        <h3>
                            Define
                        </h3>

                        <p>
                            Know what you're working toward.
                        </p>

                    </div>


                    <div class="loop-arrow">
                        →
                    </div>


                    <div class="loop-card">

                        <div class="loop-icon">
                            ◇
                        </div>

                        <h3>
                            Plan
                        </h3>

                        <p>
                            Turn your goal into a roadmap.
                        </p>

                    </div>


                    <div class="loop-arrow">
                        →
                    </div>


                    <div class="loop-card">

                        <div class="loop-icon">
                            ◆
                        </div>

                        <h3>
                            Build
                        </h3>

                        <p>
                            Complete practical learning tasks.
                        </p>

                    </div>


                    <div class="loop-arrow">
                        →
                    </div>


                    <div class="loop-card">

                        <div class="loop-icon">
                            ↗
                        </div>

                        <h3>
                            Progress
                        </h3>

                        <p>
                            Measure how far you've come.
                        </p>

                    </div>

                </div>

            </section>


            <!-- FINAL CTA -->

            <section class="how-cta">

                <div>

                    <div class="how-eyebrow">
                        YOUR TURN
                    </div>

                    <h2>
                        Stop wondering what to learn next.
                    </h2>

                    <p>
                        Start building your developer journey
                        with DEV/XP.
                    </p>

                </div>

            </section>

        </div>
        """
    )

    if st.button(
        "Start your DEV/XP journey →",
        type="primary",
        # use_container_width=True,
        key="how_start",
    ):

        st.session_state["page"] = "signup"

        st.rerun()