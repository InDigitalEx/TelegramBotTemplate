from aiogram import Router
from aiogram.types import Message

other_router = Router()


@other_router.message()
async def __inv_message(msg: Message) -> None:
    await msg.answer("test")