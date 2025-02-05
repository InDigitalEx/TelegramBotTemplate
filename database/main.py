from contextlib import asynccontextmanager

from sqlalchemy.ext.asyncio import AsyncSession, AsyncEngine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

from data import config
from utils import SingletonMeta, get_root_dir
from .models import Base


class Database(metaclass=SingletonMeta):
    def __init__(self):
        root_dir = get_root_dir()

        self._engine = create_async_engine(
            url=config.database_url.get_secret_value().format(root_dir),
            echo=True
        )
        self._async_session_maker = async_sessionmaker(
            bind=self._engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def init_models(self) -> None:
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

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
