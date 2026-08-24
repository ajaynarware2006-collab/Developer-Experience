import streamlit as st


def render_about():

    # ============================================================
    # PAGE CSS
    # ============================================================

    st.html(
        """
        <style>

        /* ========================================================
           PAGE
        ======================================================== */

        .about-page {
            width: min(1080px, 94%);
            margin: 0 auto;
            padding: 70px 0 80px;
        }


        /* ========================================================
           HERO
        ======================================================== */

        .about-hero {
            max-width: 820px;
            margin: 0 auto 90px;
            text-align: center;
        }

        .about-eyebrow {
            margin-bottom: 18px;

            color: #78d6d0;

            font-size: 11px;
            font-weight: 700;

            letter-spacing: 0.22em;
        }

        .about-hero h1 {
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

        .about-hero h1 span {
            display: block;
            color: #78d6d0;
        }

        .about-hero p {
            max-width: 680px;

            margin: 28px auto 0;

            color: #91a5aa;

            font-size: 17px;
            line-height: 1.75;
        }


        /* ========================================================
           PROBLEM SECTION
        ======================================================== */

        .about-problem {
            display: grid;

            grid-template-columns:
                0.8fr 1.2fr;

            gap: 70px;

            align-items: center;

            margin-bottom: 90px;
        }

        .about-section-label {
            margin-bottom: 15px;

            color: #78d6d0;

            font-size: 10px;
            font-weight: 700;

            letter-spacing: 0.2em;
        }

        .about-problem h2 {
            margin: 0;

            color: #f4f7f5;

            font-size: 38px;
            line-height: 1.1;

            letter-spacing: -0.035em;
        }

        .about-problem h2 span {
            color: #78d6d0;
        }

        .about-problem-text p {
            margin: 0 0 18px;

            color: #84999e;

            font-size: 15px;
            line-height: 1.8;
        }

        .about-problem-text p:last-child {
            margin-bottom: 0;
        }


        /* ========================================================
           QUOTE / STATEMENT
        ======================================================== */

        .about-statement {
            position: relative;

            padding: 45px;

            border: 1px solid
                rgba(120, 214, 208, 0.12);

            border-radius: 22px;

            background:
                linear-gradient(
                    145deg,
                    rgba(120, 214, 208, 0.065),
                    rgba(255, 255, 255, 0.018)
                );

            overflow: hidden;
        }

        .about-statement::before {
            content: "";

            position: absolute;

            width: 220px;
            height: 220px;

            top: -130px;
            right: -80px;

            border-radius: 50%;

            background:
                rgba(120, 214, 208, 0.08);

            filter: blur(35px);
        }

        .statement-mark {
            position: relative;

            color: #78d6d0;

            font-size: 52px;
            line-height: 1;

            margin-bottom: 15px;
        }

        .about-statement p {
            position: relative;

            max-width: 850px;

            margin: 0;

            color: #d8e2df;

            font-size: 25px;
            line-height: 1.45;

            font-weight: 600;

            letter-spacing: -0.02em;
        }


        /* ========================================================
           WHAT DEVXP DOES
        ======================================================== */

        .about-system {
            margin-top: 90px;
            margin-bottom: 90px;
        }

        .about-system-header {
            max-width: 650px;

            margin-bottom: 40px;
        }

        .about-system-header h2 {
            margin: 0 0 15px;

            color: #f4f7f5;

            font-size: 36px;
            line-height: 1.1;

            letter-spacing: -0.035em;
        }

        .about-system-header p {
            margin: 0;

            color: #84999e;

            font-size: 15px;
            line-height: 1.7;
        }


        /* ========================================================
           SYSTEM CARDS
        ======================================================== */

        .about-system-grid {
            display: grid;

            grid-template-columns:
                repeat(3, 1fr);

            gap: 16px;
        }

        .about-system-card {
            padding: 30px;

            min-height: 210px;

            border: 1px solid
                rgba(120, 214, 208, 0.09);

            border-radius: 18px;

            background:
                rgba(255, 255, 255, 0.025);

            transition:
                transform 0.25s ease,
                border-color 0.25s ease;
        }

        .about-system-card:hover {
            transform: translateY(-5px);

            border-color:
                rgba(120, 214, 208, 0.25);
        }

        .system-number {
            margin-bottom: 25px;

            color: #78d6d0;

            font-size: 11px;
            font-weight: 800;

            letter-spacing: 0.15em;
        }

        .about-system-card h3 {
            margin: 0 0 12px;

            color: #f4f7f5;

            font-size: 19px;
        }

        .about-system-card p {
            margin: 0;

            color: #84999e;

            font-size: 13px;
            line-height: 1.7;
        }


        /* ========================================================
           PHILOSOPHY
        ======================================================== */

        .about-philosophy {
            display: grid;

            grid-template-columns:
                1fr 1fr;

            gap: 18px;

            margin-bottom: 90px;
        }

        .philosophy-card {
            padding: 40px;

            border: 1px solid
                rgba(255, 255, 255, 0.06);

            border-radius: 20px;

            background:
                rgba(255, 255, 255, 0.02);
        }

        .philosophy-card.accent {
            border-color:
                rgba(120, 214, 208, 0.14);

            background:
                linear-gradient(
                    145deg,
                    rgba(120, 214, 208, 0.065),
                    rgba(255, 255, 255, 0.018)
                );
        }

        .philosophy-card h3 {
            margin: 0 0 15px;

            color: #f4f7f5;

            font-size: 24px;
        }

        .philosophy-card p {
            margin: 0;

            color: #84999e;

            font-size: 14px;
            line-height: 1.75;
        }


        /* ========================================================
           CURRENT STATE
        ======================================================== */

        .about-now {
            padding: 50px 45px;

            border: 1px solid
                rgba(120, 214, 208, 0.11);

            border-radius: 22px;

            background:
                linear-gradient(
                    100deg,
                    rgba(120, 214, 208, 0.07),
                    rgba(255, 255, 255, 0.018)
                );

            text-align: center;
        }

        .about-now h2 {
            margin: 0 0 12px;

            color: #f4f7f5;

            font-size: 34px;

            letter-spacing: -0.03em;
        }

        .about-now p {
            max-width: 650px;

            margin: 0 auto;

            color: #84999e;

            font-size: 14px;
            line-height: 1.75;
        }


        /* ========================================================
           RESPONSIVE
        ======================================================== */

        @media (max-width: 850px) {

            .about-problem {
                grid-template-columns: 1fr;

                gap: 35px;
            }

            .about-system-grid {
                grid-template-columns:
                    repeat(2, 1fr);
            }

        }


        @media (max-width: 650px) {

            .about-page {
                padding-top: 45px;
            }

            .about-problem h2 {
                font-size: 30px;
            }

            .about-statement {
                padding: 30px;
            }

            .about-statement p {
                font-size: 20px;
            }

            .about-system-grid {
                grid-template-columns: 1fr;
            }

            .about-philosophy {
                grid-template-columns: 1fr;
            }

            .about-now {
                padding: 38px 25px;
            }

            .about-now h2 {
                font-size: 28px;
            }

        }

        </style>
        """
    )


    # ============================================================
    # PAGE CONTENT
    # ============================================================

    st.html(
        """
        <div class="about-page">


            <!-- HERO -->

            <section class="about-hero">

                <div class="about-eyebrow">
                    DEV/XP · ABOUT
                </div>

                <h1>
                    Built for developers
                    <span>who want direction.</span>
                </h1>

                <p>
                    DEV/XP is a developer growth platform designed
                    to turn an uncertain learning journey into a
                    structured, measurable path forward.
                </p>

            </section>


            <!-- PROBLEM -->

            <section class="about-problem">

                <div>

                    <div class="about-section-label">
                        THE PROBLEM
                    </div>

                    <h2>
                        Learning to code
                        is only half
                        the battle.
                    </h2>

                </div>


                <div class="about-problem-text">

                    <p>
                        There is no shortage of tutorials,
                        courses, documentation and technologies
                        to learn.
                    </p>

                    <p>
                        The difficult part is figuring out what
                        actually matters for your goal, what you
                        should learn next, and whether you're
                        making meaningful progress.
                    </p>

                    <p>
                        DEV/XP is being built to solve that
                        problem.
                    </p>

                </div>

            </section>


            <!-- STATEMENT -->

            <section class="about-statement">

                <div class="statement-mark">
                    “
                </div>

                <p>
                    Instead of giving developers another place
                    to collect resources, DEV/XP is designed to
                    give them a system for moving forward.
                </p>

            </section>


            <!-- SYSTEM -->

            <section class="about-system">

                <div class="about-system-header">

                    <div class="about-section-label">
                        THE SYSTEM
                    </div>

                    <h2>
                        From where you are
                        to where you want to be.
                    </h2>

                    <p>
                        DEV/XP connects the important parts of
                        your developer journey into one system.
                    </p>

                </div>


                <div class="about-system-grid">


                    <div class="about-system-card">

                        <div class="system-number">
                            01 · DEFINE
                        </div>

                        <h3>
                            Your Profile
                        </h3>

                        <p>
                            Define your career goal, experience,
                            skills, target and available time.
                        </p>

                    </div>


                    <div class="about-system-card">

                        <div class="system-number">
                            02 · PLAN
                        </div>

                        <h3>
                            Your Roadmap
                        </h3>

                        <p>
                            Turn your current position and target
                            into a structured learning direction.
                        </p>

                    </div>


                    <div class="about-system-card">

                        <div class="system-number">
                            03 · BUILD
                        </div>

                        <h3>
                            Your Skills
                        </h3>

                        <p>
                            Work through practical tasks and
                            projects that move you closer to your
                            goal.
                        </p>

                    </div>


                    <div class="about-system-card">

                        <div class="system-number">
                            04 · TRACK
                        </div>

                        <h3>
                            Your Progress
                        </h3>

                        <p>
                            Keep your completed work and current
                            position visible as your journey grows.
                        </p>

                    </div>


                    <div class="about-system-card">

                        <div class="system-number">
                            05 · IMPROVE
                        </div>

                        <h3>
                            Your Direction
                        </h3>

                        <p>
                            Your developer journey can evolve as
                            your skills, goals and experience change.
                        </p>

                    </div>


                    <div class="about-system-card">

                        <div class="system-number">
                            06 · GROW
                        </div>

                        <h3>
                            Your Career
                        </h3>

                        <p>
                            The long-term goal is simple:
                            become a stronger, more capable
                            developer.
                        </p>

                    </div>


                </div>

            </section>


            <!-- PHILOSOPHY -->

            <section class="about-philosophy">


                <div class="philosophy-card accent">

                    <div class="about-section-label">
                        OUR PHILOSOPHY
                    </div>

                    <h3>
                        Less guessing.
                    </h3>

                    <p>
                        Developers shouldn't have to constantly
                        ask themselves what to learn next.
                        DEV/XP aims to make that direction clearer.
                    </p>

                </div>


                <div class="philosophy-card">

                    <div class="about-section-label">
                        OUR PHILOSOPHY
                    </div>

                    <h3>
                        More building.
                    </h3>

                    <p>
                        Knowing concepts is important. Applying
                        them is what turns knowledge into
                        development ability.
                    </p>

                </div>


            </section>


            <!-- CURRENT STATE -->

            <section class="about-now">

                <div class="about-section-label">
                    WHERE DEV/XP IS TODAY
                </div>

                <h2>
                    This is only the beginning.
                </h2>

                <p>
                    DEV/XP is actively being built into a complete
                    developer growth platform. The current system
                    focuses on authentication, developer profiles,
                    structured roadmaps and progress-oriented
                    workflows, with more capabilities being added
                    over time.
                </p>

            </section>


        </div>
        """
    )


    # ============================================================
    # CTA
    # ============================================================

    if st.button(
        "Start your DEV/XP journey →",
        type="primary",
        # use_container_width=True,
        key="about_start",
    ):

        st.session_state["page"] = "signup"

        st.rerun()