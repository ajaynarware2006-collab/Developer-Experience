from dotenv import load_dotenv
import requests
import os


load_dotenv()

API_BASE_URL = os.getenv("API_BASE_URL")


def signup_user(name, email, password):

    data = {
        "name": name,
        "email": email,
        "password": password,
    }

    response = requests.post(
        f"{API_BASE_URL}/signup",
        json=data,
    )

    if response.status_code == 409:

        error = response.json()

        raise ValueError(
            error.get(
                "detail",
                "An account with this email already exists.",
            )
        )

    if not response.ok:

        try:
            error = response.json()

            message = error.get(
                "detail",
                "Something went wrong.",
            )

        except ValueError:

            message = "Something went wrong."

        raise ValueError(message)

    return response.json()