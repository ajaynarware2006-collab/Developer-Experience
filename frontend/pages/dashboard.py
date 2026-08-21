import streamlit as st

from backend.services.roadmap_engine import generate_roadmap
from frontend.services.session_service import logout_user
from frontend.styles.dashboard_theme import load_dashboard_theme
from backend.repositories.profile_repository import get_profile_by_user_id

def render_dashboard():

    # ============================================================
    # DASHBOARD THEME
    # ============================================================

    load_dashboard_theme()

    # ============================================================
    # AUTHENTICATION
    # ============================================================

    user_id = st.session_state.get(
        "user_id"
    )

    if not user_id:

        st.session_state["page"] = "login"

        st.rerun()

    # ============================================================
    # USER DATA
    # ============================================================

    name = st.session_state.get(
        "user_name",
        "Developer",
    )

    email = st.session_state.get(
        "user_email",
        "",
    )

    # ============================================================
    # LOAD PROFILE FROM DATABASE
    # ============================================================
    user_id = st.session_state.get(
        "user_id"
    )

    if not user_id:

        st.session_state["page"] = "login"

        st.rerun()
        
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

    # ============================================================
    # PROFILE DATA
    # ============================================================

    career_goal = profile.career_goal

    experience_level = (
        profile.experience_level
    )

    timeline = profile.timeline

    skills = profile.skills

    # ============================================================
    # ROADMAP DATA
    # ============================================================

    roadmap = generate_roadmap(
        profile
    )

    phases = roadmap.get(
        "phases",
        [],
    )

    # ============================================================
    # CURRENT SESSION PROGRESS
    # ============================================================

    if "roadmap_progress" not in st.session_state:

        st.session_state[
            "roadmap_progress"
        ] = {}

    progress = st.session_state[
        "roadmap_progress"
    ]

    total_tasks = 0

    completed_tasks = 0

    for phase_index, phase in enumerate(
        phases
    ):

        topics = phase.get(
            "topics",
            [],
        )

        for topic_index, topic in enumerate(
            topics
        ):

            task_id = (
                f"phase_{phase_index}"
                f"_task_{topic_index}"
            )

            total_tasks += 1

            if progress.get(
                task_id,
                False,
            ):

                completed_tasks += 1

    if total_tasks:

        roadmap_progress = int(
            completed_tasks
            / total_tasks
            * 100
        )

    else:

        roadmap_progress = 0

    project_count = sum(
        1
        for phase in phases
        if phase.get("project")
    )

    # ============================================================
    # APPLICATION LAYOUT
    # ============================================================

    sidebar_column, content_column = st.columns(
        [0.82, 3.18],
        gap="medium",
    )


    # ============================================================
    # SIDEBAR
    # ============================================================

    with sidebar_column:

        with st.container(
            key="dashboard-sidebar"
        ):

            initial = (
                name[0].upper()
                if name
                else "D"
            )


            st.html(
                f"""
                <div class="dashboard-brand">

                    <div class="dashboard-brand-logo">
                        D
                    </div>

                    <div>

                        <div class="dashboard-brand-name">
                            DEV/XP
                        </div>

                        <div class="dashboard-brand-subtitle">
                            Developer Experience
                        </div>

                    </div>

                </div>
                """
            )


            # ----------------------------------------------------
            # OVERVIEW
            # ----------------------------------------------------

            st.html(
                """
                <div class="dashboard-section-label">
                    Overview
                </div>
                """
            )


            st.button(
                "⌂   Dashboard",
                key="dashboard_nav",
                use_container_width=True,
                disabled=True,
            )


            # ----------------------------------------------------
            # DEVELOPMENT
            # ----------------------------------------------------

            st.html(
                """
                <div class="dashboard-section-label">
                    Development
                </div>
                """
            )


            st.button(
                "⌁   Roadmap",
                key="dashboard_roadmap_nav",
                use_container_width=True,
            )

                # st.session_state["page"] = "roadmap"

                # st.rerun()


            if st.button(
                "◇   My Profile",
                key="dashboard_profile_nav",
                use_container_width=True,
            ):

                st.session_state["page"] = "profile"

                st.rerun()


            st.button(
                "▣   Learning",
                key="dashboard_learning_nav",
                use_container_width=True,
                disabled=True,
            )


            st.button(
                "◈   Projects",
                key="dashboard_projects_nav",
                use_container_width=True,
                disabled=True,
            )


            # ----------------------------------------------------
            # DEVELOPER INTELLIGENCE
            # ----------------------------------------------------

            st.html(
                """
                <div class="dashboard-section-label">
                    Developer Intelligence
                </div>
                """
            )


            st.button(
                "◆   GitHub",
                key="dashboard_github_nav",
                use_container_width=True,
                disabled=True,
            )


            st.button(
                "◆   LeetCode",
                key="dashboard_leetcode_nav",
                use_container_width=True,
                disabled=True,
            )


            st.button(
                "◌   LinkedIn",
                key="dashboard_linkedin_nav",
                use_container_width=True,
                disabled=True,
            )


            st.button(
                "✦   Developer Intelligence",
                key="dashboard_intelligence_nav",
                use_container_width=True,
                disabled=True,
            )


            # ----------------------------------------------------
            # AI
            # ----------------------------------------------------

            st.html(
                """
                <div class="dashboard-section-label">
                    AI
                </div>
                """
            )


            st.button(
                "✧   AI Mentor",
                key="dashboard_ai_nav",
                use_container_width=True,
                disabled=True,
            )


            # ----------------------------------------------------
            # SYSTEM
            # ----------------------------------------------------

            st.html(
                """
                <div class="dashboard-section-label">
                    System
                </div>
                """
            )


            st.button(
                "⚙   Settings",
                key="dashboard_settings_nav",
                use_container_width=True,
                disabled=True,
            )


            # ----------------------------------------------------
            # LOGOUT
            # ----------------------------------------------------

            if st.button(
                "↪   Logout",
                key="dashboard_logout",
                use_container_width=True,
            ):

                logout_user()

                st.rerun()


            # ----------------------------------------------------
            # USER
            # ----------------------------------------------------

            st.html(
                f"""
                <div class="dashboard-user">

                    <div class="dashboard-avatar">
                        {initial}
                    </div>

                    <div>

                        <div class="dashboard-user-name">
                            {name}
                        </div>

                        <div class="dashboard-user-email">
                            {email}
                        </div>

                    </div>

                </div>
                """
            )


    # ============================================================
    # MAIN CONTENT
    # ============================================================

    with content_column:

        with st.container(
            key="dashboard-content"
        ):

            # ----------------------------------------------------
            # HEADER
            # ----------------------------------------------------

            st.html(
                f"""
                <div class="dashboard-header">

                    <div>

                        <div class="dashboard-header-title">
                            Overview
                        </div>

                        <div class="dashboard-header-subtitle">
                            Your developer command center
                        </div>

                    </div>


                    <div class="dashboard-header-user">

                        <div class="dashboard-online">

                            <span class="dashboard-online-dot"></span>

                            DEV/XP

                        </div>


                        <div class="dashboard-avatar">
                            {(
                                name[0].upper()
                                if name
                                else "D"
                            )}
                        </div>

                    </div>

                </div>
                """
            )


            # ----------------------------------------------------
            # WELCOME
            # ----------------------------------------------------

            st.html(
                f"""
                <div class="dashboard-welcome">

                    <div class="dashboard-eyebrow">
                        Developer Overview
                    </div>

                    <h1>
                        Welcome to the DEV/XP, {name}.
                    </h1>

                    <p>
                        Here's a snapshot of your current
                        developer journey and what comes next.
                    </p>

                </div>
                """
            )


            # ----------------------------------------------------
            # SNAPSHOT
            # ----------------------------------------------------

            st.html(
                """
                <div class="dashboard-content-label">
                    Developer Snapshot
                </div>
                """
            )


            stat_1, stat_2, stat_3, stat_4 = st.columns(
                4,
                gap="small",
            )


            with stat_1:

                st.html(
                    f"""
                    <div class="dashboard-stat">

                        <div class="dashboard-stat-label">
                            CAREER GOAL
                        </div>

                        <div class="dashboard-stat-value">
                            {career_goal}
                        </div>

                        <div class="dashboard-stat-meta">
                            Your current direction
                        </div>

                    </div>
                    """
                )


            with stat_2:

                st.html(
                    f"""
                    <div class="dashboard-stat">

                        <div class="dashboard-stat-label">
                            EXPERIENCE
                        </div>

                        <div class="dashboard-stat-value">
                            {experience_level}
                        </div>

                        <div class="dashboard-stat-meta">
                            Current level
                        </div>

                    </div>
                    """
                )


            with stat_3:

                st.html(
                    f"""
                    <div class="dashboard-stat">

                        <div class="dashboard-stat-label">
                            SKILLS
                        </div>

                        <div class="dashboard-stat-value">
                            {len(skills)}
                        </div>

                        <div class="dashboard-stat-meta">
                            Skills currently recorded
                        </div>

                    </div>
                    """
                )


            with stat_4:

                st.html(
                    f"""
                    <div class="dashboard-stat">

                        <div class="dashboard-stat-label">
                            ROADMAP
                        </div>

                        <div class="dashboard-stat-value">
                            {roadmap_progress}%
                        </div>

                        <div class="dashboard-stat-meta">
                            {timeline}
                        </div>

                    </div>
                    """
                )


            st.write("")


            # ----------------------------------------------------
            # MAIN GRID
            # ----------------------------------------------------

            left_column, right_column = st.columns(
                [1.7, 1],
                gap="medium",
            )


            # ====================================================
            # LEFT
            # ====================================================

            with left_column:

                st.html(
                    """
                    <div class="dashboard-content-label">
                        Current Roadmap
                    </div>
                    """
                )


                st.html(
                    f"""
                    <div class="dashboard-card">

                        <div class="dashboard-card-title">
                            {career_goal}
                        </div>

                        <div class="dashboard-card-description">
                            Your personalized learning journey
                            toward your target career.
                        </div>


                        <div class="dashboard-progress-track">

                            <div
                                class="dashboard-progress-fill"
                                style="
                                    width:{roadmap_progress}%;
                                "
                            ></div>

                        </div>


                        <div class="dashboard-progress-meta">

                            <span>
                                {completed_tasks}
                                of
                                {total_tasks}
                                tasks completed
                            </span>

                            <span>
                                {roadmap_progress}%
                            </span>

                        </div>

                    </div>
                    """
                )


                st.write("")


                if st.button(
                    "Continue Roadmap  →",
                    key="dashboard_continue_roadmap",
                    use_container_width=True,
                ):

                    st.session_state["page"] = "roadmap"

                    st.rerun()


                st.write("")


                st.html(
                    """
                    <div class="dashboard-content-label">
                        Current Focus
                    </div>
                    """
                )


                st.html(
                    f"""
                    <div class="dashboard-focus">

                        <div class="dashboard-focus-label">
                            NEXT UP
                        </div>

                        <div class="dashboard-focus-title">
                            Build your first learning streak
                        </div>

                        <div class="dashboard-focus-text">
                            Follow your roadmap and complete
                            your next learning task to start
                            building measurable progress.
                        </div>

                    </div>
                    """
                )


            # ====================================================
            # RIGHT
            # ====================================================

            with right_column:

                st.html(
                    """
                    <div class="dashboard-content-label">
                        Developer Profile
                    </div>
                    """
                )


                st.html(
                    f"""
                    <div class="dashboard-card">

                        <div class="dashboard-card-title">
                            {name}
                        </div>

                        <div
                            class="dashboard-card-description"
                            style="
                                color:#9ED33C;
                            "
                        >
                            {career_goal}
                        </div>


                        <div
                            style="
                                margin-top:18px;
                                color:#60777B;
                                font-size:11px;
                                line-height:1.8;
                            "
                        >

                            <div>
                                Level:
                                <strong
                                    style="color:#B9C9C9;"
                                >
                                    {experience_level}
                                </strong>
                            </div>

                            <div>
                                Timeline:
                                <strong
                                    style="color:#B9C9C9;"
                                >
                                    {timeline}
                                </strong>
                            </div>

                            <div>
                                Skills:
                                <strong
                                    style="color:#B9C9C9;"
                                >
                                    {len(skills)}
                                </strong>
                            </div>

                        </div>

                    </div>
                    """
                )


                st.write("")


                if st.button(
                    "View Profile  →",
                    key="dashboard_view_profile",
                    use_container_width=True,
                ):

                    st.session_state["page"] = "profile"

                    st.rerun()


                st.write("")


                # ------------------------------------------------
                # PLATFORM SECTION
                # ------------------------------------------------

                st.html(
                    """
                    <div class="dashboard-content-label">
                        Developer Platforms
                    </div>
                    """
                )


                st.html(
                    """
                    <div class="dashboard-card">

                        <div class="platform-row">

                            <span class="platform-name">
                                GitHub
                            </span>

                            <span class="platform-status">
                                Not connected
                            </span>

                        </div>


                        <div class="platform-row">

                            <span class="platform-name">
                                LeetCode
                            </span>

                            <span class="platform-status">
                                Not connected
                            </span>

                        </div>


                        <div class="platform-row">

                            <span class="platform-name">
                                LinkedIn
                            </span>

                            <span class="platform-status">
                                Not connected
                            </span>

                        </div>

                    </div>
                    """
                )


                st.write("")


                st.html(
                    f"""
                    <div class="dashboard-card">

                        <div class="dashboard-content-label">
                            Projects
                        </div>

                        <div class="dashboard-card-title">
                            {project_count}
                        </div>

                        <div class="dashboard-card-description">
                            Recommended roadmap projects
                            available to build.
                        </div>

                    </div>
                    """
                )