from sqlalchemy import select

from backend.database.connection import SessionLocal
from backend.models.user import User


def create_user(
    name: str,
    email: str,
    password_hash: str,
):
    with SessionLocal() as db:

        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user


def get_user_by_email(email: str):

    with SessionLocal() as db:

        query = select(User).where(
            User.email == email
        )

        user = db.scalar(query)

        return user