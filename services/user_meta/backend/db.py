import os

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)
from sqlalchemy.orm import DeclarativeBase

load_dotenv(".env")
POSTGRES_URL = os.getenv(
    "PSGR_URL",
    default="postgresql+asyncpg://forest:1887@localhost:5432/markecg"
)

engine = create_async_engine(
    POSTGRES_URL,
    echo=True
)

async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Base(DeclarativeBase):  # New
    pass
