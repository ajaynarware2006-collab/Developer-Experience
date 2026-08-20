from datetime import datetime, timedelta
import hashlib
import secrets

from backend.repositories.email_verification_repository import (
    create_verification,
    get_latest_verification,
    increment_attempts,
    mark_verified,
)
from backend.database.connection import SessionLocal
from backend.models.user import User


OTP_EXPIRATION_MINUTES = 10

MAX_ATTEMPTS = 5


def generate_verification_code():

    return str(
        secrets.randbelow(900000) + 100000
    )


def hash_code(code: str):

    return hashlib.sha256(
        code.encode("utf-8")
    ).hexdigest()


def create_email_verification(
    user_id: int,
    email: str,
):

    code = generate_verification_code()

    code_hash = hash_code(code)

    expires_at = (
        datetime.now()
        + timedelta(
            minutes=OTP_EXPIRATION_MINUTES
        )
    )

    verification = create_verification(
        user_id=user_id,
        code_hash=code_hash,
        expires_at=expires_at,
    )

    return verification, code


def verify_email_code(
    user_id: int,
    entered_code: str,
):

    verification = get_latest_verification(
        user_id
    )

    if verification is None:

        return False, "No verification code found."

    if verification.verified_at is not None:

        return False, "Email is already verified."

    if verification.attempts >= MAX_ATTEMPTS:

        return False, "Too many attempts."

    if datetime.utcnow() > verification.expires_at:

        return False, "Verification code has expired."

    entered_hash = hash_code(
        entered_code.strip()
    )

    if entered_hash != verification.code_hash:

        increment_attempts(
            verification.id
        )

        return False, "Invalid verification code."

    mark_verified(
        verification.id
    )

    with SessionLocal() as db:

        user = db.get(
            User,
            user_id,
        )

        if user is not None:

            user.email_verified = True

            db.commit()

    return True, "Email verified successfully."