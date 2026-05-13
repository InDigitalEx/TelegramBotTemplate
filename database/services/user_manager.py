from sqlalchemy import select

from database import Database
from database.models import User


class UserManager:
    def __init__(self, telegram_id: int) -> None:
        self._telegram_id = telegram_id

    async def get_user(self, create: bool = False) -> User | None:
        """Get user by telegram_id.

        If `create=True` and user doesn't exist -> creates it.
        """
        async with Database().session_scope() as session:
            statement = select(User).where(User.telegram_id == self._telegram_id)
            result = await session.execute(statement)
            user = result.scalar_one_or_none()

        if user is None and create:
            return await self._create_user()
        return user

    async def _create_user(self) -> User:
        async with Database().session_scope() as session:
            user = User(telegram_id=self._telegram_id)
            session.add(user)
        return user

    @staticmethod
    async def get_all_users():
        async with Database().session_scope() as session:
            statement = select(User)
            result = await session.execute(statement)
            return result.scalars().all()
