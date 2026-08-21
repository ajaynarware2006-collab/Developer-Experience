import streamlit as st
from backend.repositories.profile_repository import (
    get_profile_by_user_id,
    update_profile,
)

# ================================================================
# CAREER OPTIONS
# ================================================================

CAREER_OPTIONS = [
    "Software Engineer",
    "AI / ML Engineer",
    "Data Scientist",
    "Full-Stack Developer",
    "Backend Developer",
    "Frontend Developer",
    "DevOps / Cloud Engineer",
    "Cybersecurity Engineer",
]


LEVEL_OPTIONS = [
    "Beginner",
    "Intermediate",
    "Advanced",
]


SKILL_OPTIONS = [
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


EXPERIENCE_OPTIONS = [
    "No professional experience",
    "Personal projects",
    "College projects",
    "Freelancing",
    "Internship",
    "Job",
]


TARGET_OPTIONS = [
    "Internship",
    "Job",
    "College placement",
    "Freelancing",
    "Career switch",
    "Learning / exploration",
]


TIMELINE_OPTIONS = [
    "3 months",
    "6 months",
    "1 year",
    "2 years",
    "No fixed deadline",
]


TIME_OPTIONS = [
    "< 1 hour/day",
    "1–2 hours/day",
    "2–4 hours/day",
    "4–6 hours/day",
    "6+ hours/day",
]


def render_profile():

    user_id = st.session_state.get(
        "user_id"
    )

    if not user_id:

        st.session_state["page"] = "login"

        st.rerun()

    # ------------------------------------------------------------
    # LOAD PROFILE FROM DATABASE
    # ------------------------------------------------------------

    profile = get_profile_by_user_id(
        user_id
    )

    if profile is None:

        st.session_state[
            "onboarding_complete"
        ] = False

        st.session_state[
            "page"
        ] = "onboarding"

        st.rerun()

    # ------------------------------------------------------------
    # CONVERT ORM OBJECT → UI DATA
    # ------------------------------------------------------------

    data = profile

    # ------------------------------------------------------------
    # EDIT STATE
    # ------------------------------------------------------------

    if "editing_profile" not in st.session_state:

        st.session_state[
            "editing_profile"
        ] = False

    editing = st.session_state[
        "editing_profile"
    ]

    # ------------------------------------------------------------
    # HEADER
    # ------------------------------------------------------------

    st.html(
        """
        <div
            style="
                text-align:center;
                max-width:750px;
                margin:55px auto 35px;
            "
        >

            <div class="devxp-eyebrow">
                DEVELOPER PROFILE
            </div>

            <h1 style="
                color:#F4F7F5;
                font-size:42px;
                font-weight:800;
                margin-top:18px;
            ">
                Here's where you stand.
            </h1>

            <p style="
                color:#91A5AA;
                font-size:17px;
                line-height:1.6;
            ">
                Your developer profile is the foundation
                of everything DEV/XP builds for you.
            </p>

        </div>
        """
    )

    if editing:

        render_edit_profile(data)

        return

    render_profile_view(data)


# =================================================================
# PROFILE VIEW
# =================================================================

def render_profile_view(data):

    career_goal = data.career_goal

    level = data.experience_level

    skills = data.skills

    experience = data.experience

    target = data.target

    timeline = data.timeline

    daily_time = data.daily_time


    # ============================================================
    # PROFILE CARD
    # ============================================================

    left, center, right = st.columns([1, 3, 1])

    with center:

        with st.container():

            # ----------------------------------------------------
            # CAREER GOAL
            # ----------------------------------------------------

            st.html(
                f"""
                <div style="
                    text-align:center;
                    padding:20px 0 30px;
                ">

                    <div style="
                        color:#71878C;
                        font-size:12px;
                        font-weight:700;
                        letter-spacing:1.5px;
                        text-transform:uppercase;
                    ">
                        CAREER GOAL
                    </div>

                    <div style="
                        color:#F4F7F5;
                        font-size:34px;
                        font-weight:850;
                        margin-top:8px;
                    ">
                        {career_goal}
                    </div>

                </div>
                """
            )


            # ----------------------------------------------------
            # QUICK STATS
            # ----------------------------------------------------

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Current Level",
                    level,
                )


            with col2:

                st.metric(
                    "Target",
                    target,
                )


            with col3:

                st.metric(
                    "Timeline",
                    timeline,
                )


            st.divider()


            # ----------------------------------------------------
            # SKILLS
            # ----------------------------------------------------

            st.html(
                """
                <div style="
                    color:#F4F7F5;
                    font-size:20px;
                    font-weight:750;
                    margin:20px 0 12px;
                ">
                    Current Skills
                </div>
                """
            )


            if skills:

                skill_html = ""

                for skill in skills:

                    skill_html += f"""
                    <span style="
                        display:inline-block;
                        padding:8px 14px;
                        margin:4px;
                        border-radius:999px;

                        background:
                            rgba(18,170,179,0.09);

                        border:
                            1px solid
                            rgba(18,170,179,0.22);

                        color:#9EDFE3;

                        font-size:14px;
                    ">
                        {skill}
                    </span>
                    """

                st.html(
                    f"""
                    <div>
                        {skill_html}
                    </div>
                    """
                )

            else:

                st.info("No skills selected.")


            # ----------------------------------------------------
            # DETAILS
            # ----------------------------------------------------

            st.html(
                f"""
                <div style="
                    display:grid;
                    grid-template-columns:1fr 1fr;
                    gap:12px;
                    margin-top:28px;
                ">

                    <div style="
                        padding:18px;
                        border-radius:14px;
                        background:
                            rgba(255,255,255,0.035);
                        border:
                            1px solid
                            rgba(255,255,255,0.07);
                    ">

                        <div style="
                            color:#71878C;
                            font-size:12px;
                            text-transform:uppercase;
                            letter-spacing:1px;
                        ">
                            Experience
                        </div>

                        <div style="
                            margin-top:7px;
                            color:#EAF2F1;
                            font-size:15px;
                            font-weight:650;
                        ">
                            {experience}
                        </div>

                    </div>


                    <div style="
                        padding:18px;
                        border-radius:14px;
                        background:
                            rgba(255,255,255,0.035);
                        border:
                            1px solid
                            rgba(255,255,255,0.07);
                    ">

                        <div style="
                            color:#71878C;
                            font-size:12px;
                            text-transform:uppercase;
                            letter-spacing:1px;
                        ">
                            Daily Learning Time
                        </div>

                        <div style="
                            margin-top:7px;
                            color:#EAF2F1;
                            font-size:15px;
                            font-weight:650;
                        ">
                            {daily_time}
                        </div>

                    </div>

                </div>
                """
            )


            # ----------------------------------------------------
            # ACTIONS
            # ----------------------------------------------------

            st.html(
                """
                <div style="
                    text-align:center;
                    margin-top:35px;
                    margin-bottom:12px;
                    color:#91A5AA;
                    font-size:14px;
                ">
                    Want to change something?
                </div>
                """
            )


            col1, col2 = st.columns(2)


            with col1:

                if st.button(
                    "✏ Edit Profile",
                    use_container_width=True,
                    key="edit_profile",
                ):

                    st.session_state["editing_profile"] = True
                    st.rerun()


            with col2:

                if st.button(
                    "Done ✦",
                    type="primary",
                    use_container_width=True,
                    key="generate_roadmap",
                ):

                    st.session_state["page"] = "dashboard"
                    st.rerun()


# =================================================================
# EDIT PROFILE
# =================================================================

def render_edit_profile(data):

    left, center, right = st.columns([1, 3, 1])

    with center:

        with st.container(key="profile-card"):

            st.html(
                """
                <div style="
                    text-align:center;
                    margin-bottom:25px;
                ">

                    <div style="
                        color:#F4F7F5;
                        font-size:28px;
                        font-weight:800;
                    ">
                        Edit your profile
                    </div>

                    <div style="
                        color:#91A5AA;
                        font-size:14px;
                        margin-top:8px;
                    ">
                        Update anything that has changed.
                    </div>

                </div>
                """
            )


            # ====================================================
            # CAREER GOAL
            # ====================================================

            current_goal = data.career_goal

            if current_goal in CAREER_OPTIONS:

                career_index = CAREER_OPTIONS.index(
                    current_goal
                )

                selected_goal = st.selectbox(
                    "Career Goal",
                    CAREER_OPTIONS,
                    index=career_index,
                    key="edit_career_goal",
                )

                final_goal = selected_goal

            else:

                st.selectbox(
                    "Career Goal",
                    ["Custom Career Goal"],
                    key="custom_goal_display",
                )

                final_goal = st.text_input(
                    "Your Career Goal",
                    value=current_goal,
                    key="edit_custom_goal",
                )


            # ====================================================
            # LEVEL
            # ====================================================

            current_level = data.experience_level

            level_index = (
                LEVEL_OPTIONS.index(current_level)
                if current_level in LEVEL_OPTIONS
                else 0
            )

            selected_level = st.selectbox(
                "Experience Level",
                LEVEL_OPTIONS,
                index=level_index,
                key="edit_level",
            )


            # ====================================================
            # SKILLS
            # ====================================================

            current_skills = data.skills

            selected_skills = st.multiselect(
                "Skills",
                SKILL_OPTIONS,
                default=[
                    skill
                    for skill in current_skills
                    if skill in SKILL_OPTIONS
                ],
                key="edit_skills",
            )


            # ====================================================
            # EXPERIENCE
            # ====================================================

            current_experience = data.experience

            experience_index = (
                EXPERIENCE_OPTIONS.index(
                    current_experience
                )
                if current_experience in EXPERIENCE_OPTIONS
                else 0
            )

            selected_experience = st.selectbox(
                "Practical Experience",
                EXPERIENCE_OPTIONS,
                index=experience_index,
                key="edit_experience",
            )


            # ====================================================
            # TARGET
            # ====================================================

            current_target = data.target

            target_index = (
                TARGET_OPTIONS.index(
                    current_target
                )
                if current_target in TARGET_OPTIONS
                else 0
            )

            selected_target = st.selectbox(
                "Current Target",
                TARGET_OPTIONS,
                index=target_index,
                key="edit_target",
            )


            # ====================================================
            # TIMELINE
            # ====================================================

            current_timeline = data.timeline

            timeline_index = (
                TIMELINE_OPTIONS.index(
                    current_timeline
                )
                if current_timeline in TIMELINE_OPTIONS
                else 0
            )

            selected_timeline = st.selectbox(
                "Target Timeline",
                TIMELINE_OPTIONS,
                index=timeline_index,
                key="edit_timeline",
            )


            # ====================================================
            # DAILY TIME
            # ====================================================

            current_time = data.daily_time

            time_index = (
                TIME_OPTIONS.index(
                    current_time
                )
                if current_time in TIME_OPTIONS
                else 0
            )

            selected_time = st.selectbox(
                "Daily Learning Time",
                TIME_OPTIONS,
                index=time_index,
                key="edit_daily_time",
            )


            # ====================================================
            # ACTIONS
            # ====================================================

            st.divider()

            col1, col2 = st.columns(2)


            # ----------------------------------------------------
            # CANCEL
            # ----------------------------------------------------

            with col1:

                if st.button(
                    "Cancel",
                    use_container_width=True,
                    key="cancel_profile_edit",
                ):

                    st.session_state["editing_profile"] = False
                    st.rerun()


            # ----------------------------------------------------
            # SAVE
            # ----------------------------------------------------

            with col2:

                if st.button(
                    "Save Changes",
                    type="primary",
                    use_container_width=True,
                    key="save_profile",
                ):

                    if not final_goal.strip():

                        st.error(
                            "Career goal cannot be empty."
                        )

                        st.stop()

                    user_id = st.session_state.get(
                        "user_id"
                    )

                    if not user_id:

                        st.error(
                            "Your session has expired. Please login again."
                        )

                        st.stop()

                    try:

                        updated_profile = update_profile(
                            user_id=user_id,
                            career_goal=final_goal.strip(),
                            experience_level=selected_level,
                            experience=selected_experience,
                            target=selected_target,
                            timeline=selected_timeline,
                            daily_time=selected_time,
                            skills=selected_skills,
                        )

                        if updated_profile is None:

                            st.error(
                                "Developer profile not found."
                            )

                            st.stop()

                        st.session_state[
                            "profile_id"
                        ] = updated_profile.id

                        st.session_state[
                            "editing_profile"
                        ] = False

                        st.success(
                            "Profile updated successfully."
                        )

                        st.rerun()

                    except Exception as error:

                        st.error(
                            f"Unable to update profile: {error}"
                        )