"""User handlers.

Contains handlers that are available for regular users (non-admin and admin alike).
"""

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from data import Messages
from database.models import User

user_router = Router()


@user_router.message(CommandStart())
async def __start(message: Message, user: User) -> None:
    """Handle `/start`.

    Expects `user` to be injected into handler context by `UserMiddleware`.
    """
    await message.answer(Messages.START.format(telegram_id=user.telegram_id))

