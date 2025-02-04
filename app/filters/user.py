from typing import Dict, Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

from database.models import User
from database.services import UserManager


class HasUserDataFilter(BaseFilter):
    async def __call__(self, message: Message) -> Dict[str, Union[User, None]]:
        user = await UserManager(message.from_user.id).get_user()
        return {'user': user}
