import bcrypt

from repositories.user_repository import (
    create_user,
    get_user_by_email,
)


def hash_password(password: str) -> str:

    password_bytes = password.encode(
        "utf-8"
    )

    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(),
    )

    return hashed.decode(
        "utf-8"
    )


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

    existing_user = get_user_by_email(
        email
    )

    if existing_user:
        raise ValueError(
            "An account with this email already exists."
        )

    password_hash = hash_password(
        password
    )

    return create_user(
        name,
        email,
        password_hash,
    )