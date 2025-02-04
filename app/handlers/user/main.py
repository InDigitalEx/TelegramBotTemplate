from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from app.filters.user import HasUserDataFilter
from data import Messages
from database.models import User

user_router = Router()

@user_router.message(CommandStart(), HasUserDataFilter())
async def __start(message: Message, user: User) -> None:
    await message.answer(
        Messages.START.format(telegram_id=user.telegram_id)
    )
