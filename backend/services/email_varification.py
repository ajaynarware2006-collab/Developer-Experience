import os
import requests
from dotenv import load_dotenv

load_dotenv()


def send_verification_email(email: str, code: str):

    api_key = os.getenv("EMAIL_API_KEY")

    payload = {
        "to": email,
        "subject": "Verify your DEV/XP account",
        "text": f"""
Welcome to DEV/XP!

Your verification code is:

{code}

This code expires in 10 minutes.

If you did not create this account, you can ignore this email.
"""
    }

    response = requests.post(
        "YOUR_EMAIL_PROVIDER_ENDPOINT",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
    )

    response.raise_for_status()