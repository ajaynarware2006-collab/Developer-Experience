from fastapi import APIRouter, HTTPException
from sqlalchemy import select
from sqlalchemy.orm import selectinload

from backend.database.connection import SessionLocal

from backend.models.roadmap import Roadmap
from backend.models.roadmap_phase import RoadmapPhase
from backend.models.roadmap_task import RoadmapTask

from backend.repositories.profile_repository import (
    get_profile_by_user_id,
)

from backend.services.roadmap_engine import (
    generate_roadmap,
)


roadmap_router = APIRouter(
    prefix="/devxp/roadmap",
    tags=["Roadmap"],
)


# =================================================================
# LOAD ROADMAP WITH ALL RELATIONSHIPS
# =================================================================

def load_roadmap(
    db,
    user_id: int,
):

    statement = (
        select(Roadmap)
        .options(
            selectinload(
                Roadmap.phases
            ).selectinload(
                RoadmapPhase.tasks
            )
        )
        .where(
            Roadmap.user_id == user_id
        )
    )

    return db.scalar(statement)


# =================================================================
# SERIALIZE ROADMAP
# =================================================================

def serialize_roadmap(
    roadmap: Roadmap,
):

    phases = []

    for phase in sorted(
        roadmap.phases,
        key=lambda item: item.phase_order,
    ):

        tasks = []

        for task in sorted(
            phase.tasks,
            key=lambda item: item.task_order,
        ):

            tasks.append(
                {
                    "id": task.id,
                    "title": task.title,
                    "completed": task.completed,
                    "task_order": task.task_order,
                }
            )

        phases.append(
            {
                "id": phase.id,
                "title": phase.title,
                "description": phase.description,
                "project": phase.project,
                "phase_order": phase.phase_order,
                "skills": [],
                "tasks": tasks,
            }
        )

    return {
        "id": roadmap.id,
        "user_id": roadmap.user_id,
        "career_goal": roadmap.career_goal,
        "timeline": roadmap.timeline,
        "progress": roadmap.progress,
        "created_at": roadmap.created_at,
        "phases": phases,
    }


# =================================================================
# GET ROADMAP
# =================================================================

@roadmap_router.get(
    "/{user_id}"
)
def get_roadmap(
    user_id: int,
):

    profile = get_profile_by_user_id(
        user_id
    )

    if profile is None:

        raise HTTPException(
            status_code=404,
            detail="Developer profile not found.",
        )

    with SessionLocal() as db:

        # ---------------------------------------------------------
        # Check whether roadmap already exists
        # ---------------------------------------------------------

        roadmap = load_roadmap(
            db,
            user_id,
        )

        # ---------------------------------------------------------
        # Create roadmap if it doesn't exist
        # ---------------------------------------------------------

        if roadmap is None:

            roadmap_data = generate_roadmap(
                profile
            )

            roadmap = Roadmap(
                user_id=user_id,
                career_goal=roadmap_data[
                    "career_goal"
                ],
                timeline=roadmap_data[
                    "timeline"
                ],
                progress=0,
            )

            db.add(roadmap)

            db.flush()

            # -----------------------------------------------------
            # Create phases
            # -----------------------------------------------------

            for phase_index, phase_data in enumerate(
                roadmap_data["phases"]
            ):

                phase = RoadmapPhase(
                    roadmap_id=roadmap.id,
                    title=phase_data["title"],
                    description=phase_data.get(
                        "description"
                    ),
                    project=phase_data.get(
                        "project"
                    ),
                    phase_order=phase_index,
                )

                db.add(phase)

                db.flush()

                # -------------------------------------------------
                # Create tasks
                # -------------------------------------------------

                for task_index, topic in enumerate(
                    phase_data.get(
                        "topics",
                        [],
                    )
                ):

                    task = RoadmapTask(
                        phase_id=phase.id,
                        title=topic,
                        task_order=task_index,
                        completed=False,
                    )

                    db.add(task)

            db.commit()

            # -----------------------------------------------------
            # Reload roadmap with phases + tasks
            # -----------------------------------------------------

            roadmap = load_roadmap(
                db,
                user_id,
            )

        if roadmap is None:

            raise HTTPException(
                status_code=500,
                detail="Unable to load roadmap.",
            )

        return serialize_roadmap(
            roadmap
        )


# =================================================================
# UPDATE TASK
# =================================================================

@roadmap_router.patch(
    "/{user_id}/tasks/{task_id}"
)
def update_task(
    user_id: int,
    task_id: int,
    completed: bool,
):

    with SessionLocal() as db:

        task = db.get(
            RoadmapTask,
            task_id,
        )

        if task is None:

            raise HTTPException(
                status_code=404,
                detail="Task not found.",
            )

        phase = db.get(
            RoadmapPhase,
            task.phase_id,
        )

        if phase is None:

            raise HTTPException(
                status_code=404,
                detail="Roadmap phase not found.",
            )

        roadmap = db.get(
            Roadmap,
            phase.roadmap_id,
        )

        if roadmap is None:

            raise HTTPException(
                status_code=404,
                detail="Roadmap not found.",
            )

        # ---------------------------------------------------------
        # Ownership check
        # ---------------------------------------------------------

        if roadmap.user_id != user_id:

            raise HTTPException(
                status_code=403,
                detail="You cannot modify this roadmap.",
            )

        # ---------------------------------------------------------
        # Update task
        # ---------------------------------------------------------

        task.completed = completed

        db.flush()

        # ---------------------------------------------------------
        # Recalculate roadmap progress
        # ---------------------------------------------------------

        statement = (
            select(RoadmapTask)
            .join(
                RoadmapPhase,
                RoadmapPhase.id
                == RoadmapTask.phase_id,
            )
            .where(
                RoadmapPhase.roadmap_id
                == roadmap.id
            )
        )

        all_tasks = db.scalars(
            statement
        ).all()

        total_tasks = len(
            all_tasks
        )

        completed_tasks = sum(
            1
            for item in all_tasks
            if item.completed
        )

        if total_tasks:

            roadmap.progress = int(
                completed_tasks
                / total_tasks
                * 100
            )

        else:

            roadmap.progress = 0

        db.commit()

        return {
            "success": True,
            "task_id": task.id,
            "completed": task.completed,
            "progress": roadmap.progress,
        }