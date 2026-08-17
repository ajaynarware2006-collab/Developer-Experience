from backend.database.connection import get_connection
# from sqlalchemy import 

def create_developer_profile(
    user_id: int,
    career_goal: str,
    experience_level: str,
    experience: str,
    target: str,
    timeline: str,
    daily_time: str,
    skills: list[str],
):
    profile_query = """
        INSERT INTO developer_profiles (
            user_id,
            career_goal,
            experience_level,
            experience,
            target,
            timeline,
            daily_time
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        RETURNING id;
    """

    skills_query = """
        INSERT INTO profile_skills (
            profile_id,
            skill
        )
        VALUES (%s, %s)
        ON CONFLICT (profile_id, skill)
        DO NOTHING;
    """

    with get_connection() as connection:

        with connection.cursor() as cursor:

            # Create developer profile
            cursor.execute(
                profile_query,
                (
                    user_id,
                    career_goal,
                    experience_level,
                    experience,
                    target,
                    timeline,
                    daily_time,
                ),
            )

            profile_id = cursor.fetchone()[0]

            # Save skills
            for skill in skills:

                cursor.execute(
                    skills_query,
                    (
                        profile_id,
                        skill,
                    ),
                )

        connection.commit()

    return profile_id

# def get_profile():


