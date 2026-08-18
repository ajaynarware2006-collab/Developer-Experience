from sqlalchemy import select

from database.connection import SessionLocal
from models.user import User


with SessionLocal() as session:

    statement = select(User)

    users = session.scalars(
        statement
    ).all()

    for user in users:

        print(
            user.id,
            user.name,
            user.email
        )