from backend.repositories.user_repository import (
    create_user,
    get_user_by_email,
)

from backend.models.user import User
import bcrypt


def hash_password(password: str) -> str:

    password_bytes = password.encode("utf-8")

    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(),
    )

    return hashed.decode("utf-8")


def verify_password(
    password: str,
    password_hash: str,
) -> bool:

    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8"),
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