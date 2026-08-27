import requests
import os
from dotenv import load_dotenv

load_dotenv()



API_BASE_URL = os.getenv("API_BASE_URL")


def health_check():

    response = requests.get(
        f"{API_BASE_URL}/health",
        timeout=5,
    )

    response.raise_for_status()

    return response.json()