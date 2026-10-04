from fastapi import (
    Cookie,
    Header,
    HTTPException,
    status,
)

import bcrypt

from backend.repositories.user_repository import (
    get_user_by_email,
)

from backend.services.jwt_service import (
    verify_access_token,
)

from backend.models.user import User


def verify_password(
    password: str,
    password_hash: str,
) -> bool:

    return bcrypt.checkpw(
        password.encode("utf-8"),
        password_hash.encode("utf-8"),
    )


def get_current_user(
    access_token: str | None = Cookie(
        default=None
    ),
    authorization: str | None = Header(
        default=None
    ),
):

    token = access_token

    # --------------------------------------------------------
    # PREFER BEARER TOKEN
    # --------------------------------------------------------

    if authorization:

        if authorization.startswith(
            "Bearer "
        ):

            token = authorization[
                7:
            ]

    # --------------------------------------------------------
    # NO TOKEN
    # --------------------------------------------------------

    if not token:

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Not authenticated",
        )

    # --------------------------------------------------------
    # VERIFY TOKEN
    # --------------------------------------------------------

    try:

        payload = verify_access_token(
            token
        )

        user_id = int(
            payload["sub"]
        )

        return user_id

    except (
        ValueError,
        KeyError,
        TypeError,
    ):

        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired token",
        )


def authenticate_user(
    email: str,
    password: str,
) -> User | None:

    email = (
        email
        .strip()
        .lower()
    )

    user = get_user_by_email(
        email
    )

    if not user:

        return None

    if not verify_password(
        password,
        user.password_hash,
    ):

        return None

    return user