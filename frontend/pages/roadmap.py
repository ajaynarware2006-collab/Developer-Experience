import streamlit as st

from services.roadmap_engine import generate_roadmap


def render_roadmap():

    # ============================================================
    # PROFILE
    # ============================================================

    profile = st.session_state.get("onboarding", {})

    if not profile:

        st.warning(
            "Developer profile not found."
        )

        if st.button(
            "Go to Profile",
            type="primary",
        ):
            st.session_state["page"] = "profile"
            st.rerun()

        return


    # ============================================================
    # ROADMAP
    # ============================================================

    roadmap_data = generate_roadmap(profile)

    phases = roadmap_data["phases"]

    career_goal = roadmap_data["career_goal"]
    timeline = roadmap_data["timeline"]


    # ============================================================
    # INITIALIZE TASK PROGRESS
    # ============================================================

    if "roadmap_progress" not in st.session_state:

        st.session_state["roadmap_progress"] = {}


    progress = st.session_state["roadmap_progress"]


    # ============================================================
    # HEADER
    # ============================================================

    st.html(
        f"""
        <div
            style="
                max-width:1100px;
                margin:55px auto 35px;
            "
        >

            <div class="devxp-eyebrow">
                YOUR DEVELOPER ROADMAP
            </div>

            <h1
                style="
                    color:#F4F7F5;
                    font-size:44px;
                    font-weight:850;
                    letter-spacing:-1.5px;
                    margin-top:18px;
                "
            >
                Your path to
                <span style="color:#9ED33C;">
                    {career_goal}
                </span>
            </h1>

            <p
                style="
                    color:#91A5AA;
                    font-size:17px;
                    line-height:1.7;
                    max-width:700px;
                "
            >
                Learn, practice and build your way toward
                your career goal.
            </p>

        </div>
        """
    )


    # ============================================================
    # CALCULATE OVERALL PROGRESS
    # ============================================================

    total_tasks = 0
    completed_tasks = 0


    for phase_index, phase in enumerate(phases):

        for topic_index, topic in enumerate(
            phase["topics"]
        ):

            task_id = create_task_id(
                phase_index,
                topic_index,
            )

            total_tasks += 1

            if progress.get(task_id, False):
                completed_tasks += 1


    if total_tasks > 0:

        overall_progress = int(
            completed_tasks / total_tasks * 100
        )

    else:

        overall_progress = 0


    # ============================================================
    # SUMMARY CARD
    # ============================================================

    left, center, right = st.columns(
        [1, 4, 1]
    )

    with center:

        with st.container(
            key="roadmap-summary"
        ):

            col1, col2, col3 = st.columns(3)


            with col1:

                st.metric(
                    "Career Goal",
                    career_goal,
                )


            with col2:

                st.metric(
                    "Timeline",
                    timeline,
                )


            with col3:

                st.metric(
                    "Progress",
                    f"{overall_progress}%",
                )


            st.progress(
                overall_progress / 100
            )


            st.html(
                f"""
                <div
                    style="
                        text-align:center;
                        color:#71878C;
                        font-size:13px;
                        margin-top:7px;
                    "
                >
                    {completed_tasks} of
                    {total_tasks}
                    learning tasks completed
                </div>
                """
            )


    # ============================================================
    # SECTION TITLE
    # ============================================================

    st.html(
        """
        <div
            style="
                max-width:1100px;
                margin:65px auto 25px;
            "
        >

            <div
                style="
                    color:#12AAB3;
                    font-size:11px;
                    font-weight:750;
                    letter-spacing:2px;
                    text-transform:uppercase;
                "
            >
                LEARNING JOURNEY
            </div>

            <h2
                style="
                    color:#F4F7F5;
                    font-size:30px;
                    font-weight:800;
                    margin-top:8px;
                "
            >
                Your roadmap
            </h2>

        </div>
        """
    )


    # ============================================================
    # PHASES
    # ============================================================

    for phase_index, phase in enumerate(phases):

        render_phase(
            phase,
            phase_index,
            progress,
        )


    # ============================================================
    # BOTTOM
    # ============================================================

    st.html(
        """
        <div
            style="
                max-width:700px;
                margin:65px auto 15px;
                text-align:center;
                color:#71878C;
                font-size:14px;
            "
        >
            Your roadmap will evolve as you progress.
        </div>
        """
    )


    col1, col2, col3 = st.columns(
        [1, 1.4, 1]
    )

    with col2:

        if st.button(
            "← Back to Profile",
            use_container_width=True,
            key="roadmap_back_profile",
        ):

            st.session_state["page"] = "profile"
            st.rerun()


# =================================================================
# PHASE
# =================================================================

def render_phase(
    phase,
    phase_index,
    progress,
):

    topics = phase["topics"]

    completed = 0

    for topic_index, topic in enumerate(topics):

        task_id = create_task_id(
            phase_index,
            topic_index,
        )

        if progress.get(task_id, False):
            completed += 1


    if topics:

        phase_progress = int(
            completed / len(topics) * 100
        )

    else:

        phase_progress = 0


    if phase_progress == 100:

        status = "✓ Completed"
        status_color = "#9ED33C"

    elif phase_progress > 0:

        status = "→ In Progress"
        status_color = "#12AAB3"

    else:

        status = "○ Upcoming"
        status_color = "#71878C"


    # ============================================================
    # PHASE CONTAINER
    # ============================================================

    with st.container(
        key=f"phase_{phase_index}"
    ):

        st.html(
            f"""
            <div
                style="
                    padding:28px;
                    margin-bottom:8px;

                    border-radius:20px;

                    background:
                        rgba(20,32,34,0.62);

                    border:
                        1px solid
                        rgba(255,255,255,0.08);

                    backdrop-filter:
                        blur(18px);

                    -webkit-backdrop-filter:
                        blur(18px);

                    box-shadow:
                        0 20px 50px
                        rgba(0,0,0,0.22);
                "
            >

                <div
                    style="
                        display:flex;
                        justify-content:space-between;
                        align-items:flex-start;
                        gap:20px;
                    "
                >

                    <div>

                        <div
                            style="
                                color:#71878C;
                                font-size:11px;
                                font-weight:750;
                                letter-spacing:1.5px;
                                text-transform:uppercase;
                            "
                        >
                            PHASE {phase_index + 1}
                        </div>

                        <div
                            style="
                                color:#F4F7F5;
                                font-size:25px;
                                font-weight:800;
                                margin-top:6px;
                            "
                        >
                            {phase["title"]}
                        </div>

                        <div
                            style="
                                color:#91A5AA;
                                font-size:14px;
                                line-height:1.6;
                                margin-top:7px;
                            "
                        >
                            {phase["description"]}
                        </div>

                    </div>

                    <div
                        style="
                            color:{status_color};
                            font-size:12px;
                            font-weight:750;
                            white-space:nowrap;
                        "
                    >
                        {status}
                    </div>

                </div>


                <div
                    style="
                        margin-top:20px;
                    "
                >

                    <div
                        style="
                            display:flex;
                            justify-content:space-between;
                            margin-bottom:7px;
                        "
                    >

                        <span
                            style="
                                color:#71878C;
                                font-size:12px;
                            "
                        >
                            Phase Progress
                        </span>

                        <span
                            style="
                                color:#9EDFE3;
                                font-size:12px;
                                font-weight:700;
                            "
                        >
                            {phase_progress}%
                        </span>

                    </div>

                    <div
                        style="
                            height:7px;
                            border-radius:20px;
                            background:
                                rgba(255,255,255,0.06);
                            overflow:hidden;
                        "
                    >

                        <div
                            style="
                                width:{phase_progress}%;
                                height:100%;
                                border-radius:20px;

                                background:
                                    linear-gradient(
                                        90deg,
                                        #087B84,
                                        #12AAB3,
                                        #9ED33C
                                    );

                                transition:
                                    width 0.3s ease;
                            "
                        ></div>

                    </div>

                </div>

            </div>
            """
        )


        # ========================================================
        # SKILLS
        # ========================================================

        skill_html = ""

        for skill in phase["skills"]:

            skill_html += f"""
            <span
                style="
                    display:inline-block;
                    padding:7px 12px;
                    margin:3px;

                    border-radius:999px;

                    background:
                        rgba(18,170,179,0.08);

                    border:
                        1px solid
                        rgba(18,170,179,0.18);

                    color:#9EDFE3;
                    font-size:13px;
                "
            >
                {skill}
            </span>
            """


        st.html(
            f"""
            <div
                style="
                    margin:
                        0 0 18px 25px;
                "
            >

                <div
                    style="
                        color:#71878C;
                        font-size:11px;
                        font-weight:750;
                        letter-spacing:1px;
                        text-transform:uppercase;
                        margin-bottom:7px;
                    "
                >
                    Skills
                </div>

                {skill_html}

            </div>
            """
        )


        # ========================================================
        # TOPICS
        # ========================================================

        st.html(
            """
            <div
                style="
                    margin:
                        25px 0 10px 25px;

                    color:#F4F7F5;
                    font-size:18px;
                    font-weight:750;
                "
            >
                Learning Tasks
            </div>
            """
        )


        for topic_index, topic in enumerate(topics):

            task_id = create_task_id(
                phase_index,
                topic_index,
            )

            checked = progress.get(
                task_id,
                False,
            )


            new_value = st.checkbox(
                topic,
                value=checked,
                key=f"task_checkbox_{task_id}",
            )


            if new_value != checked:

                progress[task_id] = new_value

                st.rerun()


        # ========================================================
        # PROJECT
        # ========================================================

        st.html(
            f"""
            <div
                style="
                    margin:
                        25px 0 25px 25px;

                    padding:18px;

                    border-radius:14px;

                    background:
                        rgba(239,104,67,0.035);

                    border:
                        1px solid
                        rgba(239,104,67,0.12);
                "
            >

                <div
                    style="
                        color:#EF6843;
                        font-size:11px;
                        font-weight:750;
                        letter-spacing:1px;
                        text-transform:uppercase;
                    "
                >
                    Recommended Project
                </div>

                <div
                    style="
                        color:#EAF2F1;
                        font-size:16px;
                        font-weight:700;
                        margin-top:6px;
                    "
                >
                    {phase["project"]}
                </div>

            </div>
            """
        )


# =================================================================
# TASK ID
# =================================================================

def create_task_id(
    phase_index,
    topic_index,
):

    return (
        f"phase_{phase_index}"
        f"_task_{topic_index}"
    )