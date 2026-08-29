from fastapi import APIRouter, HTTPException

from backend.repositories.profile_repository import (
    get_profile_by_user_id,
)

from backend.services.roadmap_engine import (
    generate_roadmap,
)


dashboard_router = APIRouter(
    prefix="/devxp/dashboard",
    tags=["Dashboard"],
)


@dashboard_router.get("/{user_id}")
def get_dashboard(
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

    roadmap = generate_roadmap(
        profile
    )

    total_tasks = sum(
        len(phase["topics"])
        for phase in roadmap["phases"]
    )

    return {
        "user": {
            "id": user_id,
        },
        "profile": {
            "career_goal": profile.career_goal,
            "experience_level": profile.experience_level,
            "timeline": profile.timeline,
            "skills": [
                skill.skill
                for skill in profile.skills
            ],
        },
        "roadmap": {
            "career_goal": roadmap["career_goal"],
            "timeline": roadmap["timeline"],
            "total_tasks": total_tasks,
        },
    }