from aiogram import Dispatcher, Bot
from aiogram.types import Message
from repositories.response_repository import ResponseRepository
from bot import db

async def __wifi_status(message: Message) -> None:
    response_repository: ResponseRepository = ResponseRepository(db)
    
    response = response_repository.get_last_response()
    
    message = f"""
        Останній звіт від плати про стан інтернету:\n
        Сила сигналу: {response.signal_strength}\n
        MAC-адреса: {response.mac_address}\n
        Час створення: {response.created_at}\n
        
        """
          
    await message.reply(message)
        

async def __avg_signal_strength_last_24_hours(message: Message) -> None:
    response_repository: ResponseRepository = ResponseRepository(db)
    
    avg_signal_strength = response_repository.get_avg_signal_strength_last_24_hours()
    
    await message.reply(f"Середня сила сигналу за останні 24 години: {avg_signal_strength}.")


def register_wifi_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__wifi_status, commands=["wifi_status"])
    dp.register_message_handler(__avg_signal_strength_last_24_hours, commands=["avg_wifi_status_last_24_hours"])
