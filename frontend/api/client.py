import os

import requests
from dotenv import load_dotenv


load_dotenv()


API_BASE_URL = os.getenv(
    "API_BASE_URL",
    "http://127.0.0.1:8000",
)


session = requests.Session()


def api_request(
    method: str,
    endpoint: str,
    **kwargs,
):

    url = (
        f"{API_BASE_URL.rstrip('/')}"
        f"/{endpoint.lstrip('/')}"
    )

    response = session.request(
        method,
        url,
        timeout=30,
        **kwargs,
    )

    return response


def get(
    endpoint: str,
    **kwargs,
):

    return api_request(
        "GET",
        endpoint,
        **kwargs,
    )


def post(
    endpoint: str,
    **kwargs,
):

    return api_request(
        "POST",
        endpoint,
        **kwargs,
    )


def put(
    endpoint: str,
    **kwargs,
):

    return api_request(
        "PUT",
        endpoint,
        **kwargs,
    )


def delete(
    endpoint: str,
    **kwargs,
):

    return api_request(
        "DELETE",
        endpoint,
        **kwargs,
    )


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