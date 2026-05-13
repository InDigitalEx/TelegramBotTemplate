from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from data import config
from utils import SingletonMeta, get_root_dir
from .models import Base


class Database(metaclass=SingletonMeta):
    """SQLAlchemy async database singleton.

    Provides:
    - async engine creation
    - session maker
    - model initialization helpers
    """

    def __init__(self):
        """Create database engine and session factory."""
        root_dir = get_root_dir()

        self._engine = create_async_engine(
            url=config.database_url.get_secret_value().format(root_dir),
            echo=True,
        )
        self._async_session_maker = async_sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=True,
        )

    async def init_models(self) -> None:
        """Create all tables defined in SQLAlchemy models."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def drop_models(self) -> None:
        """Drop all tables defined in SQLAlchemy models."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)

    async def clear_models(self) -> None:
        """Drop and recreate all tables."""
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)

    async def dispose(self) -> None:
        """Dispose engine connections."""
        await self.engine.dispose()


    @asynccontextmanager
    async def session_scope(self):
        session = self.session_maker()
        try:
            yield session
            await session.commit()
        except:
            await session.rollback()
            raise
        finally:
            await session.close()

    @property
    def session_maker(self) -> async_sessionmaker[AsyncSession]:
        return self._async_session_maker

    @property
    def engine(self) -> AsyncEngine:
        return self._engine
