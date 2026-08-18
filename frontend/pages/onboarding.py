import streamlit as st
from backend.repositories.profile_repository import (
    create_profile
)
from backend.repositories.profile_repository import create_profile

def render_onboarding():

    # ============================================================
    # INITIAL STATE
    # ============================================================

    if "onboarding_step" not in st.session_state:
        st.session_state["onboarding_step"] = 1

    if "onboarding" not in st.session_state:
        st.session_state["onboarding"] = {
            "career_goal": "",
            "experience_level": "",
            "skills": [],
            "experience": "",
            "target": "",
            "timeline": "",
            "daily_time": "",
        }

    data = st.session_state["onboarding"]
    step = st.session_state["onboarding_step"]


    # ============================================================
    # HEADER
    # ============================================================

    st.html(
        """
        <div class="onboarding-header"
             style="
                text-align:center;
                max-width:750px;
                margin:55px auto 35px;
             ">

            <div class="devxp-eyebrow">
                DEV / XP
            </div>

            <h1 style="
                color:#F4F7F5;
                font-size:42px;
                font-weight:800;
                margin-top:18px;
            ">
                Let's understand you.
            </h1>

            <p style="
                color:#91A5AA;
                font-size:17px;
                line-height:1.6;
            ">
                Tell us about yourself so DEV/XP can
                build a roadmap around your actual goals.
            </p>

        </div>
        """
    )


    # ============================================================
    # PROGRESS
    # ============================================================

    st.progress(step / 6)

    st.html(
        f"""
        <div style="
            text-align:center;
            color:#71878C;
            font-size:14px;
            margin-top:8px;
            margin-bottom:30px;
        ">
            Step {step} of 6
        </div>
        """
    )


    # ============================================================
    # CENTER
    # ============================================================

    left, center, right = st.columns([1.1, 2.8, 1.1])

    with center:

        # ========================================================
        # STEP 1 — CAREER GOAL
        # ========================================================

        if step == 1:

            st.html(
                """
                <div class="onboarding-question">

                    <h2 style="
                        color:#F4F7F5;
                        font-size:30px;
                    ">
                        What do you want to become?
                    </h2>

                    <p style="
                        color:#91A5AA;
                        font-size:16px;
                    ">
                        Your career goal will become the
                        foundation of your personalized roadmap.
                    </p>

                </div>
                """
            )

            goals = [
                "Software Engineer",
                "AI / ML Engineer",
                "Data Scientist",
                "Full-Stack Developer",
                "Backend Developer",
                "Frontend Developer",
                "DevOps / Cloud Engineer",
                "Cybersecurity Engineer",
                "Other",
            ]

            current_goal = data["career_goal"]

            selected_goal = st.selectbox(
                "Career Goal",
                goals,
                index=(
                    goals.index(current_goal)
                    if current_goal in goals
                    else 0
                ),
                key="career_goal_select",
            )


            custom_goal = ""

            if selected_goal == "Other":

                custom_goal = st.text_input(
                    "Tell us your career goal",
                    value=(
                        current_goal
                        if current_goal
                        and current_goal not in goals
                        else ""
                    ),
                    placeholder="e.g. GenAI Engineer, AI Product Engineer...",
                    key="custom_career_goal",
                )


            if st.button(
                "Continue →",
                type="primary",
                use_container_width=True,
                key="onboarding_step1",
            ):

                if selected_goal == "Other":

                    if not custom_goal.strip():
                        st.error(
                            "Please enter your career goal."
                        )
                        st.stop()

                    data["career_goal"] = custom_goal.strip()

                else:

                    data["career_goal"] = selected_goal

                st.session_state["onboarding_step"] = 2
                st.rerun()


        # ========================================================
        # STEP 2 — LEVEL
        # ========================================================

        elif step == 2:

            st.html(
                """
                <div class="onboarding-question">

                    <h2 style="
                        color:#F4F7F5;
                        font-size:30px;
                    ">
                        Where are you right now?
                    </h2>

                    <p style="
                        color:#91A5AA;
                        font-size:16px;
                    ">
                        Be honest. DEV/XP will use this
                        to avoid teaching you things you already know.
                    </p>

                </div>
                """
            )

            levels = [
                "Beginner",
                "Intermediate",
                "Advanced",
            ]

            selected = st.radio(
                "Experience Level",
                levels,
                index=(
                    levels.index(data["experience_level"])
                    if data["experience_level"] in levels
                    else 0
                ),
                label_visibility="collapsed",
            )


            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "← Back",
                    use_container_width=True,
                    key="onboarding_back_2",
                ):

                    st.session_state["onboarding_step"] = 1
                    st.rerun()


            with col2:

                if st.button(
                    "Continue →",
                    type="primary",
                    use_container_width=True,
                    key="onboarding_next_2",
                ):

                    data["experience_level"] = selected

                    st.session_state["onboarding_step"] = 3
                    st.rerun()


        # ========================================================
        # STEP 3 — SKILLS
        # ========================================================

        elif step == 3:

            st.html(
                """
                <div class="onboarding-question">

                    <h2 style="
                        color:#F4F7F5;
                        font-size:30px;
                    ">
                        What do you already know?
                    </h2>

                    <p style="
                        color:#91A5AA;
                        font-size:16px;
                    ">
                        Select everything you have worked with.
                    </p>

                </div>
                """
            )

            skills = [
                "Python",
                "Java",
                "JavaScript",
                "C++",
                "SQL",
                "HTML / CSS",
                "React",
                "FastAPI",
                "Django",
                "Machine Learning",
                "Deep Learning",
                "Git / GitHub",
                "Docker",
                "Cloud",
                "Streamlit",
                "PostgreSQL",
            ]

            selected_skills = []

            for index, skill in enumerate(skills):

                if st.checkbox(
                    skill,
                    value=skill in data["skills"],
                    key=f"onboarding_skill_{index}",
                ):

                    selected_skills.append(skill)


            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "← Back",
                    use_container_width=True,
                    key="onboarding_back_3",
                ):

                    st.session_state["onboarding_step"] = 2
                    st.rerun()


            with col2:

                if st.button(
                    "Continue →",
                    type="primary",
                    use_container_width=True,
                    key="onboarding_next_3",
                ):

                    data["skills"] = selected_skills

                    st.session_state["onboarding_step"] = 4
                    st.rerun()


        # ========================================================
        # STEP 4 — EXPERIENCE
        # ========================================================

        elif step == 4:

            st.html(
                """
                <div class="onboarding-question">

                    <h2 style="
                        color:#F4F7F5;
                        font-size:30px;
                    ">
                        What experience do you have?
                    </h2>

                    <p style="
                        color:#91A5AA;
                        font-size:16px;
                    ">
                        This helps us understand your practical exposure.
                    </p>

                </div>
                """
            )

            options = [
                "No professional experience",
                "Personal projects",
                "College projects",
                "Freelancing",
                "Internship",
                "Job",
            ]

            selected = st.radio(
                "Experience",
                options,
                index=(
                    options.index(data["experience"])
                    if data["experience"] in options
                    else 0
                ),
                label_visibility="collapsed",
            )


            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "← Back",
                    use_container_width=True,
                    key="onboarding_back_4",
                ):

                    st.session_state["onboarding_step"] = 3
                    st.rerun()


            with col2:

                if st.button(
                    "Continue →",
                    type="primary",
                    use_container_width=True,
                    key="onboarding_next_4",
                ):

                    data["experience"] = selected

                    st.session_state["onboarding_step"] = 5
                    st.rerun()


        # ========================================================
        # STEP 5 — TARGET
        # ========================================================

        elif step == 5:

            st.html(
                """
                <div class="onboarding-question">

                    <h2 style="
                        color:#F4F7F5;
                        font-size:30px;
                    ">
                        What are you working toward?
                    </h2>

                    <p style="
                        color:#91A5AA;
                        font-size:16px;
                    ">
                        Your roadmap should have a destination.
                    </p>

                </div>
                """
            )

            targets = [
                "Internship",
                "Job",
                "College placement",
                "Freelancing",
                "Career switch",
                "Learning / exploration",
            ]

            selected_target = st.radio(
                "Target",
                targets,
                index=(
                    targets.index(data["target"])
                    if data["target"] in targets
                    else 0
                ),
                label_visibility="collapsed",
            )


            timelines = [
                "3 months",
                "6 months",
                "1 year",
                "2 years",
                "No fixed deadline",
            ]

            selected_timeline = st.selectbox(
                "Target Timeline",
                timelines,
                index=(
                    timelines.index(data["timeline"])
                    if data["timeline"] in timelines
                    else 0
                ),
            )


            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "← Back",
                    use_container_width=True,
                    key="onboarding_back_5",
                ):

                    st.session_state["onboarding_step"] = 4
                    st.rerun()


            with col2:

                if st.button(
                    "Continue →",
                    type="primary",
                    use_container_width=True,
                    key="onboarding_next_5",
                ):

                    data["target"] = selected_target
                    data["timeline"] = selected_timeline

                    st.session_state["onboarding_step"] = 6
                    st.rerun()


        # ========================================================
        # STEP 6 — TIME
        # ========================================================

        elif step == 6:

            st.html(
                """
                <div class="onboarding-question">

                    <h2 style="
                        color:#F4F7F5;
                        font-size:30px;
                    ">
                        How much time can you invest?
                    </h2>

                    <p style="
                        color:#91A5AA;
                        font-size:16px;
                    ">
                        We'll make your roadmap realistic
                        for your available time.
                    </p>

                </div>
                """
            )

            options = [
                "< 1 hour/day",
                "1–2 hours/day",
                "2–4 hours/day",
                "4–6 hours/day",
                "6+ hours/day",
            ]

            selected = st.radio(
                "Daily Learning Time",
                options,
                index=(
                    options.index(data["daily_time"])
                    if data["daily_time"] in options
                    else 0
                ),
                label_visibility="collapsed",
            )


            col1, col2 = st.columns(2)

            with col1:

                if st.button(
                    "← Back",
                    use_container_width=True,
                    key="onboarding_back_6",
                ):

                    st.session_state["onboarding_step"] = 5
                    st.rerun()


            with col2:

                if st.button(
                    "Review My Profile ✦",
                    type="primary",
                    use_container_width=True,
                    key="onboarding_finish",
                ):

                    data["daily_time"] = selected

                    user_id = st.session_state.get(
                        "user_id"
                    )

                    if not user_id:

                        st.error(
                            "Your session has expired. Please login again."
                        )

                        st.stop()


                    try:

                        profile = create_profile(
                            user_id=user_id,
                            career_goal=data["career_goal"],
                            experience_level=data["experience_level"],
                            experience=data["experience"],
                            target=data["target"],
                            timeline=data["timeline"],
                            daily_time=data["daily_time"],
                            skills=data["skills"],
                        )

                        st.session_state["profile_id"] = profile.id

                        st.session_state["onboarding_complete"] = True

                        st.session_state["page"] = "profile"

                        st.rerun()


                    except Exception as error:

                        st.error(
                            f"Unable to save your profile: {error}"
                        )
