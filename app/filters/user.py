from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.models import User
from database.services import UserManager


class HasUserDataFilter(BaseFilter):
    async def __call__(self, message: Message) -> Union[None, User]:
        user_manager = UserManager(message.from_user.id)
        return await user_manager.get_user()
