from frontend.api.client import (
    api_request,
    get_error_message,
)


def send_verification_code(
    email: str,
    user_id: int,
):

    response = api_request(
        "POST",
        "/devxp/sendcode",
        json={
            "email": email,
            "user_id": user_id,
        },
    )

    if not response.ok:

        raise ValueError(
            get_error_message(
                response,
                "Unable to send verification code.",
            )
        )

    return response.json()


def verify_varification_code(
    user_id: int,
    entered_code: str,
):

    response = api_request(
        "POST",
        "/devxp/verifycode",
        json={
            "user_id": user_id,
            "code_entered": entered_code,
        },
    )

    if not response.ok:

        raise ValueError(
            get_error_message(
                response,
                "Verification failed.",
            )
        )

    result = response.json()

    return (
        result["success"],
        result["message"],
    )