from sqlalchemy import select , delete

from backend.database.connection import SessionLocal
from backend.models.user import User
from backend.services.auth_service import hash_password


async def create_user(
    name: str,
    email: str,
    password: str,
):
    password_hash = hash_password(password)

    with SessionLocal() as db:


        user = User(
            name=name,
            email=email,
            password_hash=password_hash,
        )

        await db.add(user)
        db.commit()
        db.refresh(user)

        return user


async def delete_user_by_id(id:int):
    with SessionLocal() as db:
        query = delete(User).where(User.id == id)
        result =await db.execute(query)
        db.commit()



async def get_user_by_email(email: str):

    with SessionLocal() as db:

        query = select(User).where(
            User.email == email
        )

        user =await db.scalar(query)

        return user

    
async def get_user_by_id(user_id: int):

    with SessionLocal() as db:

        query = select(User).where(
            User.id == user_id
        )

        user =await db.scalar(query)

        return user

