from aiogram import Bot, Dispatcher
from aiogram.types import Message
from bot import db
from repositories.wifi_repository import WifiRepository


async def __send_status(message: Message) -> None:
    wifi_repository: WifiRepository = WifiRepository(db)

    wifi_status = "є" if wifi_repository.get_last_wifi_record().is_powered else "немає"

    await message.reply(f"Статус світла: {wifi_status}.")


async def __wifi_statuses_last_24_hours(message: Message) -> None:
    wifi_repository: WifiRepository = WifiRepository(db)

    wifi_statuses = wifi_repository.get_wifi_records_last_24_hours()

    await message.reply(f"Записи стану світла за останні 24 години: {wifi_statuses}.")


async def __wifi_statuses_last_week(message: Message) -> None:
    wifi_repository: WifiRepository = WifiRepository(db)

    wifi_statuses = wifi_repository.get_wifi_records_last_week()

    await message.reply(f"Записи стану світла за останній тиждень: {wifi_statuses}.")


def register_wifi_handlers(dp: Dispatcher) -> None:
    dp.register_message_handler(__send_status, commands=["status"])
    dp.register_message_handler(
        __wifi_statuses_last_24_hours, commands=["status_last_24_hours"]
    )
    dp.register_message_handler(
        __wifi_statuses_last_week, commands=["status_last_week"]
    )
