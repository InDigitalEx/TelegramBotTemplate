from aiogram import Router

from app.middlewares.user import UserMiddleware


def register_main_middlewares(router: Router) -> None:
    """Register middlewares."""
    # For /start and other user-dependent handlers
    router.message.middleware(UserMiddleware(create=True))
