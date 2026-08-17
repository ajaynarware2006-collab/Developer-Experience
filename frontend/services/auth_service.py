from backend.repositories.user_repository import (
    create_user,
    get_user_by_email,
)

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


def register_user(
    name: str,
    email: str,
    password: str,
):

    email = email.strip().lower()

    existing_user = get_user_by_email(email)

    if existing_user:
        raise ValueError(
            "An account with this email already exists."
        )

    password_hash = hash_password(password)

    return create_user(
        name.strip(),
        email,
        password_hash,
    )


def authenticate_user(
    email: str,
    password: str,
):

    email = email.strip().lower()

    user = get_user_by_email(email)

    if not user:
        return None

    user_id = user[0]
    name = user[1]
    user_email = user[2]
    password_hash = user[3]

    if not verify_password(
        password,
        password_hash,
    ):
        return None

    return {
        "id": user_id,
        "name": name,
        "email": user_email,
    }