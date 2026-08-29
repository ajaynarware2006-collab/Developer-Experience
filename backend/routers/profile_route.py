from fastapi import APIRouter, HTTPException

from backend.repositories.profile_repository import (
    create_profile,
    get_profile_by_user_id,
    update_profile,
)

from backend.schemas.developer_profile import (
    DeveloperProfileCreate,
    DeveloperProfileUpdate,
    DeveloperProfileResponse,
)


profile_router = APIRouter(
    prefix="/devxp/profile",
    tags=["Profile"],
)


def serialize_profile(profile):

    return {
        "id": profile.id,
        "user_id": profile.user_id,
        "career_goal": profile.career_goal,
        "experience_level": profile.experience_level,
        "experience": profile.experience,
        "target": profile.target,
        "timeline": profile.timeline,
        "daily_time": profile.daily_time,
        "skills": [
            skill.skill
            for skill in profile.skills
        ],
    }


# ============================================================
# GET PROFILE
# ============================================================

@profile_router.get(
    "/{user_id}",
    response_model=DeveloperProfileResponse,
)
def get_profile(user_id: int):

    profile = get_profile_by_user_id(
        user_id
    )

    if profile is None:

        raise HTTPException(
            status_code=404,
            detail="Developer profile not found.",
        )

    return serialize_profile(profile)


# ============================================================
# CREATE PROFILE
# ============================================================

@profile_router.post(
    "/{user_id}",
    response_model=DeveloperProfileResponse,
)
def create_user_profile(
    user_id: int,
    data: DeveloperProfileCreate,
):

    existing_profile = get_profile_by_user_id(
        user_id
    )

    if existing_profile:

        raise HTTPException(
            status_code=409,
            detail="Developer profile already exists.",
        )

    profile = create_profile(
        user_id=user_id,
        career_goal=data.career_goal,
        experience_level=data.experience_level,
        experience=data.experience,
        target=data.target,
        timeline=data.timeline,
        daily_time=data.daily_time,
        skills=data.skills,
    )

    return serialize_profile(profile)


# ============================================================
# UPDATE PROFILE
# ============================================================

@profile_router.put(
    "/{user_id}",
    response_model=DeveloperProfileResponse,
)
def update_user_profile(
    user_id: int,
    data: DeveloperProfileUpdate,
):

    existing_profile = get_profile_by_user_id(
        user_id
    )

    if existing_profile is None:

        raise HTTPException(
            status_code=404,
            detail="Developer profile not found.",
        )

    profile = update_profile(
        user_id=user_id,
        career_goal=data.career_goal,
        experience_level=data.experience_level,
        experience=data.experience,
        target=data.target,
        timeline=data.timeline,
        daily_time=data.daily_time,
        skills=data.skills or [],
    )

    return serialize_profile(profile)