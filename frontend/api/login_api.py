from frontend.api.client import (
    api_request,
)


def authenticate_user_api(
    email,
    password,
):

    response = api_request(
        "POST",
        "/devxp/authenticate_user",
        json={
            "email": email,
            "password": password,
        },
    )

    if response.status_code == 401:

        return None

    response.raise_for_status()

    return response.json()