import logging

from aiogram import Bot, Dispatcher
from aiogram import Router
from aiogram.exceptions import TelegramAPIError
from aiogram.fsm.storage.memory import MemoryStorage

from app.filters import register_all_filters
from app.handlers import handlers_router
from app.middlewares import register_all_middlewares
from data import Env
from database.models import register_models

# Routers
main_router = Router()


# Observers
@main_router.startup()
async def __on_startup(router: Router) -> None:
    logging.info('Bot starts')

    # Include routers
    router.include_router(handlers_router)

    register_all_filters(router)
    register_all_middlewares(router)


@main_router.shutdown()
async def __on_shutdown(router: Router) -> None:
    logging.info('Bot shutdown')


# Run bot polling method
async def run_bot() -> None:
    # Register DB models
    register_models()

    # Start telegram bot
    try:
        bot = Bot(token=Env.TOKEN, parse_mode='HTML')
        dp = Dispatcher(storage=MemoryStorage())

        dp.include_routers(main_router)

        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot, on_startup=__on_startup, on_shutdown=__on_shutdown)
    except TelegramAPIError as telegram_exception:
        logging.error(telegram_exception)
