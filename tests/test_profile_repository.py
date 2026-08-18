from backend.repositories.profile_repository import (
    create_profile,
    get_profile_by_user_id,
)


profile = create_profile(
    user_id=1,
    career_goal="Backend Developer",
    experience_level="Beginner",
    experience="Python, SQL, PostgreSQL",
    target="Backend Developer",
    timeline="6 months",
    daily_time="3 hours",
    skills=[
        "Python",
        "PostgreSQL",
        "SQLAlchemy",
        "FastAPI",
    ],
)

print(
    profile.id,
    profile.career_goal,
)


saved_profile = get_profile_by_user_id(1)

print(
    saved_profile.id,
    saved_profile.career_goal,
)