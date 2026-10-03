from sqlalchemy import select, delete
from sqlalchemy.exc import IntegrityError

from backend.database.connection import SessionLocal
from backend.models.user import User

import bcrypt


def hash_password(password: str) -> str:

    password_bytes = password.encode("utf-8")

    hashed = bcrypt.hashpw(
        password_bytes,
        bcrypt.gensalt(),
    )

    return hashed.decode("utf-8")


def get_user_by_email(email: str):

    with SessionLocal() as db:

        query = select(User).where(
            User.email == email
        )

        return db.scalar(query)


def get_user_by_github_id(github_id: str):

    with SessionLocal() as db:

        query = select(User).where(
            User.github_id == github_id
        )

        return db.scalar(query)


def get_user_by_google_id(google_id: str):

    with SessionLocal() as db:

        query = select(User).where(
            User.google_id == google_id
        )

        return db.scalar(query)


def create_user(
    name: str,
    email: str,
    password: str,
    github_id: str | None = None,
    github_username: str | None = None,
    github_avatar_url: str | None = None,
    github_access_token: str | None = None,
    google_id: str | None = None,
    google_avatar_url: str | None = None,
):

    password_hash = hash_password(
        password
    )

    with SessionLocal() as db:

        user = User(
            name=name.strip(),
            email=email.strip().lower(),
            password_hash=password_hash,

            github_id=github_id,
            github_username=github_username,
            github_avatar_url=github_avatar_url,
            github_access_token=github_access_token,

            google_id=google_id,
            google_avatar_url=google_avatar_url,
        )

        db.add(user)

        try:

            db.commit()

        except IntegrityError:

            db.rollback()

            raise ValueError(
                "An account with this email already exists."
            )

        db.refresh(user)

        return user


def update_github_data(
    user_id: int,
    github_id: str,
    github_username: str,
    github_avatar_url: str | None,
    github_access_token: str,
):

    with SessionLocal() as db:

        user = db.scalar(
            select(User).where(
                User.id == user_id
            )
        )

        if user is None:
            return None

        user.github_id = github_id
        user.github_username = github_username
        user.github_avatar_url = github_avatar_url
        user.github_access_token = github_access_token

        db.commit()
        db.refresh(user)

        return user


def update_google_data(
    user_id: int,
    google_id: str,
    google_avatar_url: str | None,
):

    with SessionLocal() as db:

        user = db.scalar(
            select(User).where(
                User.id == user_id
            )
        )

        if user is None:
            return None

        user.google_id = google_id
        user.google_avatar_url = google_avatar_url

        db.commit()
        db.refresh(user)

        return user


def delete_user_by_id(id: int):

    with SessionLocal() as db:

        query = delete(User).where(
            User.id == id
        )

        db.execute(query)

        db.commit()


def get_user_by_id(user_id: int):

    with SessionLocal() as db:

        query = select(User).where(
            User.id == user_id
        )

        return db.scalar(query)