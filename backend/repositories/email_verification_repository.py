from datetime import datetime

from sqlalchemy import select

from backend.database.connection import SessionLocal
from backend.models.verification_code import (
    EmailVerification,
)


def create_verification(
    user_id: int,
    code_hash: str,
    expires_at: datetime,
):

    with SessionLocal() as db:

        verification = EmailVerification(
            user_id=user_id,
            code_hash=code_hash,
            expires_at=expires_at,
        )

        db.add(verification)

        db.commit()

        db.refresh(verification)

        return verification


def get_latest_verification(
    user_id: int,
):

    with SessionLocal() as db:

        statement = (
            select(EmailVerification)
            .where(
                EmailVerification.user_id
                == user_id
            )
            .order_by(
                EmailVerification.created_at.desc()
            )
        )

        return db.scalar(statement)


def increment_attempts(
    verification_id: int,
):

    with SessionLocal() as db:

        verification = db.get(
            EmailVerification,
            verification_id,
        )

        if verification is None:
            return

        verification.attempts += 1

        db.commit()


def mark_verified(
    verification_id: int,
):

    with SessionLocal() as db:

        verification = db.get(
            EmailVerification,
            verification_id,
        )

        if verification is None:
            return

        verification.verified_at = (
            datetime.utcnow()
        )

        db.commit()