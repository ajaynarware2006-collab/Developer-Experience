from sqlalchemy import select

from backend.database.connection import SessionLocal
from backend.models.user import User
from backend.services.verification_service import create_email_verification
from backend.services.email_service import send_verification_code

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

    
def get_user_by_id(user_id: int):

    with SessionLocal() as db:

        query = select(User).where(
            User.id == user_id
        )

        user = db.scalar(query)

        return user

