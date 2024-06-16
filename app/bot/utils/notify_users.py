import logging
from aiogram import Bot
from repositories.user_repository import UserRepository


async def notify_users(bot: Bot, message: str):
    user_repository = UserRepository()
    user_ids = await user_repository.get_all_telegram_ids()

    for user_id in user_ids:
        try:
            await bot.send_message(user_id, message)
        except Exception as e:
            logging.error(f"Error sending message to {user_id}: {e}")
