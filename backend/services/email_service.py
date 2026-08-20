import os
import smtplib

from email.message import EmailMessage

from dotenv import load_dotenv


load_dotenv()


SMTP_HOST = os.getenv(
    "SMTP_HOST",
    "smtp.gmail.com",
)

SMTP_PORT = int(
    os.getenv(
        "SMTP_PORT",
        "587",
    )
)

SMTP_EMAIL = os.getenv(
    "SMTP_EMAIL",
)

SMTP_PASSWORD = os.getenv(
    "SMTP_PASSWORD",
)


def send_verification_code(
    recipient_email: str,
    verification_code: str,
):

    if not SMTP_EMAIL:
        raise RuntimeError(
            "SMTP_EMAIL is not configured."
        )

    if not SMTP_PASSWORD:
        raise RuntimeError(
            "SMTP_PASSWORD is not configured."
        )

    message = EmailMessage()

    message["Subject"] = (
        "DEV/XP Email Verification Code"
    )

    message["From"] = SMTP_EMAIL

    message["To"] = recipient_email

    message.set_content(
        f"""
            Hello,

            Welcome to DEV/XP.

            Your email verification code is:

            {verification_code}

            This code will expire in 10 minutes.

            If you did not create a DEV/XP account,
            you can safely ignore this email.

            — DEV/XP
        """
            )

    with smtplib.SMTP(
        SMTP_HOST,
        SMTP_PORT,
    ) as server:

        server.starttls()

        server.login(
            SMTP_EMAIL,
            SMTP_PASSWORD,
        )

        server.send_message(
            message
        )
    