from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from bot.handlers import register_all_handlers
from bot.utils import notify_users
from bot.config import BotConfig

bot_config = BotConfig()

API_TOKEN = bot_config.get_token()

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

def init_bot():
    register_all_handlers(dp)

async def start_polling():
    await dp.start_polling()

async def notify_all_users(message: str):
    await notify_users(bot, message)
