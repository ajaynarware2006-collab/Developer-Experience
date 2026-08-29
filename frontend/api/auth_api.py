from frontend.api.client import (
    api_request,
    get_error_message,
)


def signup_user(
    name,
    email,
    password,
):

    response = api_request(
        "POST",
        "/devxp/signup",
        json={
            "name": name,
            "email": email,
            "password": password,
        },
    )

    if response.status_code == 409:

        raise ValueError(
            get_error_message(
                response,
                "An account with this email already exists.",
            )
        )

    if not response.ok:

        raise ValueError(
            get_error_message(response)
        )

    return response.json()