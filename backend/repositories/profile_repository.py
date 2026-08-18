from sqlalchemy import select

from backend.database.connection import SessionLocal
from backend.models.developer_profile import DeveloperProfile
from backend.models.profile_skill import ProfileSkill


def create_profile(
    user_id: int,
    career_goal: str,
    experience_level: str,
    experience: str,
    target: str,
    timeline: str,
    daily_time: str,
    skills: list[str],
):
    with SessionLocal() as db:

        profile = DeveloperProfile(
            user_id=user_id,
            career_goal=career_goal,
            experience_level=experience_level,
            experience=experience,
            target=target,
            timeline=timeline,
            daily_time=daily_time,
        )

        db.add(profile)

        db.flush()

        for skill in skills:

            profile_skill = ProfileSkill(
                profile_id=profile.id,
                skill=skill,
            )

            db.add(profile_skill)

        db.commit()

        db.refresh(profile)

        return profile


def get_profile_by_user_id(user_id: int):

    with SessionLocal() as db:

        return (
            db.query(DeveloperProfile)
            .filter(DeveloperProfile.user_id == user_id)
            .first()
        )