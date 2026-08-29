from sqlalchemy import select , delete
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

        user = db.scalar(query)

        return user


def create_user(
    name: str,
    email: str,
    password: str,
):

    password_hash = hash_password(
        password
    )

    with SessionLocal() as db:

        user = User(
            name=name.strip(),
            email=email.strip().lower(),
            password_hash=password_hash,
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



def delete_user_by_id(id:int):
    with SessionLocal() as db:
        query = delete(User).where(User.id == id)
        result = db.execute(query)
        db.commit()


    
def get_user_by_id(user_id: int):

    with SessionLocal() as db:

        query = select(User).where(
            User.id == user_id
        )

        user =db.scalar(query)

        return user

