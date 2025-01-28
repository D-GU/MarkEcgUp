from sqlalchemy.ext.asyncio import (
    create_async_engine, async_sessionmaker, AsyncSession
)

from sqlalchemy.orm import DeclarativeBase

engine = create_async_engine(
    'postgresql+asyncpg://forest:1887@localhost:5432/markecgup',
    echo=True
)

async_session_maker = async_sessionmaker(
    engine,
    expire_on_commit=False,
    class_=AsyncSession
)


class Base(DeclarativeBase):  # New
    pass
