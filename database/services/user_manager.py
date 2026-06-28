from sqlalchemy import select

from database import Database
from database.models import User


class UserManager:
    """High-level operations for `User` model."""

    def __init__(self, telegram_id: int) -> None:
        """Initialize manager for a specific Telegram user."""
        self._telegram_id = telegram_id

    async def get_user(self, create: bool = True) -> User | None:
        """Load a user by `telegram_id`.

        Args:
            create: If `True`, create user in DB when it doesn't exist.

        Returns:
            User instance or `None` when user doesn't exist and `create=False`.
        """
        async with Database().session_scope() as session:
            statement = select(User).where(User.telegram_id == self._telegram_id)
            result = await session.execute(statement)
            user = result.scalar_one_or_none()

        if user is None and create:
            return await self._create_user()
        return user

    async def _create_user(self) -> User:
        """Create a new user with the manager's `telegram_id`."""
        async with Database().session_scope() as session:
            user = User(telegram_id=self._telegram_id)
            session.add(user)
        return user

    @staticmethod
    async def get_all_users() -> list[User]:
        """Return all users from DB."""
        async with Database().session_scope() as session:
            statement = select(User)
            result = await session.execute(statement)
            return result.scalars().all()
