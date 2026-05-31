from collections.abc import AsyncGenerator

from sqlalchemy.pool import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from .config import get_settings


settings = get_settings()

engine_options = {"pool_pre_ping": True}

if settings.async_database_url.startswith("postgresql+asyncpg"):
    engine_options["connect_args"] = {
        "ssl": "require",
        "statement_cache_size": 0,
    }
    engine_options["poolclass"] = NullPool

engine = create_async_engine(settings.async_database_url, **engine_options)
SessionLocal = async_sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    async with SessionLocal() as session:
        yield session
