from aiogram import Dispatcher, Bot
from aiogram.types import Message
from repositories.user_repository import UserRepository
from typing import List


async def __start(message: Message) -> None:

    user_repository: UserRepository = UserRepository()

    first_name: str = message.from_user.first_name
    last_name: str = message.from_user.last_name
    telegram_id: int = message.from_user.id
    telegram_tag: str = message.from_user.username

    user_repository.create_user(
        telegram_tag=telegram_tag,
        telegram_id=telegram_id,
        first_name=first_name,
        last_name=last_name,
        is_admin=False,
    )
    bot: Bot = message.bot
    await bot.send_message(message.from_user.id, "/status - перевірка світла.")


async def __commands(message: Message) -> None:

    bot: Bot = message.bot

    commands: List[str] = [
        "/start - початок роботи.",
        "/status - перевірка світла.",
        "/status_last_24_hours - перевірка стану світла за останні 24 години.",
        "/status_last_week - перевірка стану світла за останній тиждень.",
        "/wifi_status - перевірка стану інтернету.",
        "/avg_wifi_status_last_24_hours - середня сила сигналу за останні 24 години.",
    ]

    await bot.send_message(message.from_user.id, "\n".join(commands))


def register_users_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__start, commands=["start"])
    dp.register_message_handler(__commands, commands=["commands"])
