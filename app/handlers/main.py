from aiogram import Router

from app.handlers.admin import admin_router
from app.handlers.other import other_router
from app.handlers.user import user_router

handlers_router = Router()


@handlers_router.startup()
async def __handlers_router_startup(router: Router) -> None:
    router.include_routers(admin_router, other_router, user_router)
