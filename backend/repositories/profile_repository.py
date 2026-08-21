from sqlalchemy import select
from sqlalchemy.orm import selectinload

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

            clean_skill = skill.strip()

            if not clean_skill:
                continue

            profile.skills.append(
                ProfileSkill(
                    skill=clean_skill
                )
            )

        db.commit()

        db.refresh(profile)

        return profile


def get_profile_by_user_id(user_id: int):

    with SessionLocal() as db:

        statement = (
            select(DeveloperProfile)
            .options(
                selectinload(
                    DeveloperProfile.skills
                )
            )
            .where(
                DeveloperProfile.user_id == user_id
            )
        )

        return db.scalar(statement)


def update_profile(
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

        statement = (
            select(DeveloperProfile)
            .options(
                selectinload(
                    DeveloperProfile.skills
                )
            )
            .where(
                DeveloperProfile.user_id == user_id
            )
        )

        profile = db.scalar(statement)

        if profile is None:
            return None

        profile.career_goal = career_goal
        profile.experience_level = experience_level
        profile.experience = experience
        profile.target = target
        profile.timeline = timeline
        profile.daily_time = daily_time

        # Remove old skills
        profile.skills.clear()

        # IMPORTANT:
        # Force SQLAlchemy to execute the DELETEs
        # before inserting the new skills.
        db.flush()

        # Add new skills
        for skill in skills:

            clean_skill = skill.strip()

            if not clean_skill:
                continue

            profile.skills.append(
                ProfileSkill(
                    skill=clean_skill
                )
            )

        db.commit()

        db.refresh(profile)

        return profile