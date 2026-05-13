from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from data import Messages
from database.models import User

user_router = Router()

# UserMiddleware(create=True) injects `user` into handler data
@user_router.message(CommandStart())
async def __start(message: Message, user: User) -> None:
    await message.answer(
        Messages.START.format(telegram_id=user.telegram_id)
    )
