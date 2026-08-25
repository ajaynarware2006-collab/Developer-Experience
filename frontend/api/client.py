import requests


API_BASE_URL = "http://localhost:8000"


def health_check():

    response = requests.get(
        f"{API_BASE_URL}/health",
        timeout=5,
    )

    response.raise_for_status()

    return response.json()