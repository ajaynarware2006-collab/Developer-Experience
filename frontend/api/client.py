import os

import requests
from dotenv import load_dotenv


load_dotenv()


API_BASE_URL = os.getenv(
    "API_BASE_URL"
)


if not API_BASE_URL:

    raise RuntimeError(
        "API_BASE_URL is not configured."
    )


def api_request(
    method: str,
    endpoint: str,
    **kwargs,
):

    url = (
        f"{API_BASE_URL.rstrip('/')}"
        f"/{endpoint.lstrip('/')}"
    )

    response = requests.request(
        method,
        url,
        timeout=30,
        **kwargs,
    )

    return response


def get_error_message(
    response,
    default="Something went wrong.",
):

    try:

        data = response.json()

        return data.get(
            "detail",
            default,
        )

    except ValueError:

        return default