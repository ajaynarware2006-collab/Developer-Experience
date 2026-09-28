from backend.repositories.user_repository import (
    get_user_by_email,
)

from fastapi import Cookie, HTTPException, status
from backend.services.jwt_service import verify_access_token

from backend.models.user import User
import bcrypt



def verify_password(
    password: str,
    password_hash: str,
) -> bool:

    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8"),
    )

def get_current_user(
    access_token: str | None = Cookie(default=None)
):
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated"
        )

    try:
        payload = verify_access_token(access_token)

        user_id = int(payload["sub"])

        return user_id

    except (ValueError, KeyError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token"
        )

def authenticate_user(
    email: str,
    password: str,
) -> User:

    email = email.strip().lower()

    user = get_user_by_email(email)

    if not user:
        return None

    if not verify_password(
        password,
        user.password_hash,
    ):
        return None

    return user