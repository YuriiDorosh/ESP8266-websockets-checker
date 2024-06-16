from aiogram import Dispatcher
from bot.handlers.user_handlers import register_users_handlers
from bot.handlers.response_handlers import register_wifi_handlers
from bot.handlers.wifi_handlers import register_wifi_handlers


def register_all_handlers(dp: Dispatcher) -> None:
    handlers: list = [
        register_users_handlers,
        register_wifi_handlers,
        register_wifi_handlers,
    ]

    for handler in handlers:
        handler(dp)
