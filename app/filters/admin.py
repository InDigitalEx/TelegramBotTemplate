from aiogram.filters import Filter
from aiogram.types import Message

from database.models import User


class IsAdminFilter(Filter):
    async def __call__(
        self,
        message: Message,
        user: User | None = None,
    ) -> bool:
        # Require injected `user` from middleware to avoid extra DB queries.
        return bool(user and user.is_admin)
