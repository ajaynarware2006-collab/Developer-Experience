from frontend.api.client import (
    api_request,
    get_error_message,
)


def get_roadmap(
    user_id: int,
):

    response = api_request(
        "GET",
        f"/devxp/roadmap/{user_id}",
    )

    # ---------------------------------------------------------
    # Profile missing
    # ---------------------------------------------------------

    if response.status_code == 404:

        raise ValueError(
            get_error_message(
                response,
                "Roadmap could not be found.",
            )
        )

    # ---------------------------------------------------------
    # Other errors
    # ---------------------------------------------------------

    if not response.ok:

        raise ValueError(
            get_error_message(
                response,
                "Unable to load roadmap.",
            )
        )

    return response.json()


def update_task(
    user_id: int,
    task_id: int,
    completed: bool,
):

    response = api_request(
        "PATCH",
        f"/devxp/roadmap/{user_id}/tasks/{task_id}",
        params={
            "completed": completed,
        },
    )

    if not response.ok:

        raise ValueError(
            get_error_message(
                response,
                "Unable to update task.",
            )
        )

    return response.json()