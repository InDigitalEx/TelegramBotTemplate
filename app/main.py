import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.enums import ParseMode
from aiogram.exceptions import AiogramError
from aiogram.fsm.storage.memory import MemoryStorage
from aiohttp import ClientError as AiohttpClientError

from app.handlers import handlers_router
from app.middlewares import register_main_middlewares
from data import config
from database import Database


async def __on_startup() -> None:
    # Register DB models
    await Database().init_models()

    logging.info('Bot starts')


async def __on_shutdown() -> None:
    # Gracefully dispose SQLAlchemy engine
    await Database().dispose()

    logging.info('Bot shutdown')


async def run_bot() -> None:
    """Run telegram bot (start polling)."""
    async with AiohttpSession(proxy=None) as session:
        try:
            bot: Bot = Bot(
                token=config.bot_token.get_secret_value(),
                session=session,
                default=DefaultBotProperties(parse_mode=ParseMode.HTML),
            )

            dp = Dispatcher(storage=MemoryStorage())
            dp.include_router(handlers_router)
            register_main_middlewares(dp)

            dp.startup.register(__on_startup)
            dp.shutdown.register(__on_shutdown)

            await bot.delete_webhook(drop_pending_updates=True)
            return await dp.start_polling(bot)

        except (AiohttpClientError, AiogramError) as exception:
            logging.error(exception)
            await session.close()
