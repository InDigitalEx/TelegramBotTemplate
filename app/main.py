import logging

from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramAPIError
from aiogram.fsm.storage.memory import MemoryStorage

from app.handlers import handlers_router
from app.middlewares import register_main_middlewares
from data import Env
from database.models import register_database_models


async def __on_startup(router: Router) -> None:
    router.include_router(handlers_router)
    register_main_middlewares(router)

    logging.info('Bot starts')


async def __on_shutdown(router: Router) -> None:
    logging.info('Bot shutdown')


# Run bot polling method
async def run_bot() -> None:
    # Register DB models
    register_database_models()

    # Start telegram bot
    try:
        bot = Bot(token=Env.TOKEN, parse_mode=ParseMode.HTML)
        dp = Dispatcher(storage=MemoryStorage())
        dp.startup.register(__on_startup)
        dp.shutdown.register(__on_shutdown)

        await bot.delete_webhook(drop_pending_updates=True)
        return await dp.start_polling(bot)
    except TelegramAPIError as telegram_exception:
        logging.error(telegram_exception)
