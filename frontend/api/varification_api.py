from dotenv import load_dotenv
import requests
import os


load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")


def send_verification_code(
    email: str,
    user_id: int,
):

    data = {
        "email": email,
        "user_id": user_id,
    }

    response = requests.post(
        f"{API_BASE_URL}/sendcode",
        json=data,
    )

    if not response.ok:

        try:
            error = response.json()

            message = error.get(
                "detail",
                "Unable to send verification code.",
            )

        except ValueError:

            message = "Unable to send verification code."

        raise ValueError(message)

    return response.json()


def verify_varification_code(
    user_id: int,
    entered_code: str,
):

    data = {
        "user_id": user_id,
        "code_entered": entered_code,
    }

    response = requests.post(
        f"{API_BASE_URL}/verifycode",
        json=data,
    )

    if not response.ok:

        try:
            error = response.json()

            message = error.get(
                "detail",
                "Verification failed.",
            )

        except ValueError:

            message = "Verification failed."

        raise ValueError(message)

    result = response.json()

    return (
        result["success"],
        result["message"],
    )