from types import SimpleNamespace

from frontend.api.client import (
    api_request,
    get_error_message,
)


def _profile_object(data):

    return SimpleNamespace(
        id=data["id"],
        user_id=data["user_id"],
        career_goal=data["career_goal"],
        experience_level=data["experience_level"],
        experience=data["experience"],
        target=data["target"],
        timeline=data["timeline"],
        daily_time=data["daily_time"],
        skills=data.get("skills", []),
    )

def get_profile(user_id: int):

    response = api_request(
        "GET",
        f"/devxp/profile/{user_id}",
    )

    if response.status_code == 404:

        return None

    if not response.ok:

        raise ValueError(
            get_error_message(
                response,
                "Unable to load profile.",
            )
        )

    return _profile_object(
        response.json()
    )


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

    response = api_request(
        "POST",
        f"/devxp/profile/{user_id}",
        json={
            "career_goal": career_goal,
            "experience_level": experience_level,
            "experience": experience,
            "target": target,
            "timeline": timeline,
            "daily_time": daily_time,
            "skills": skills,
        },
    )

    if not response.ok:

        raise ValueError(
            get_error_message(
                response,
                "Unable to create profile.",
            )
        )

    return _profile_object(
        response.json()
    )


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

    response = api_request(
        "PUT",
        f"/devxp/profile/{user_id}",
        json={
            "career_goal": career_goal,
            "experience_level": experience_level,
            "experience": experience,
            "target": target,
            "timeline": timeline,
            "daily_time": daily_time,
            "skills": skills,
        },
    )

    if not response.ok:

        raise ValueError(
            get_error_message(
                response,
                "Unable to update profile.",
            )
        )

    return _profile_object(
        response.json()
    )