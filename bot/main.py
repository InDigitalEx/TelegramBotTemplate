from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import TelegramAPIError
from aiogram.utils import executor
from loguru import logger

from bot.database.models import register_models
from bot.filters import register_all_filters
from bot.handlers import register_all_handlers
from bot.misc import Env


async def __on_startup(dp: Dispatcher) -> None:
    logger.info('Bot starts')

    register_models()
    register_all_filters(dp)
    register_all_handlers(dp)


async def __on_shutdown(dp: Dispatcher) -> None:
    logger.info('Bot shutdown')


def start_bot() -> None:
    try:
        bot = Bot(token=Env.TOKEN, parse_mode='HTML')
        dp = Dispatcher(bot, storage=MemoryStorage())
        executor.start_polling(dp, skip_updates=True, on_startup=__on_startup, on_shutdown=__on_shutdown)
    except TelegramAPIError as telegram_exception:
        logger.error(telegram_exception)
