from __future__ import annotations

from typing import Any, Awaitable, Callable, Dict

from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject

from database.models import User
from database.services import UserManager


class UserMiddleware(BaseMiddleware):
    """Inject `user` into handler data and optionally create it."""

    def __init__(self, *, create: bool = False) -> None:
        super().__init__()
        self._create = create

    async def __call__(
        self,
        handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: Dict[str, Any],
    ) -> Any:
        if not isinstance(event, Message):
            return await handler(event, data)

        telegram_id = event.from_user.id
        user: User | None = await UserManager(telegram_id).get_user(create=self._create)
        data['user'] = user

        return await handler(event, data)
