from sqlalchemy.ext.asyncio import create_async_engine , async_sessionmaker , AsyncSession

import os
from dotenv import load_dotenv


load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")


engine = create_async_engine(DATABASE_URL,echo=False,pool_pre_ping=True)

SessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

async def get_db():
    async with SessionLocal() as db:
        yield db