#bot.py
from aiogram import Bot, Dispatcher
from bot.handlers import start, booking, cancel_booking, info, free_slots
from config.settings import settings
from aiogram.fsm.storage.memory import MemoryStorage

bot = Bot(settings.BOT_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(storage=storage)
dp.include_router(start.router)
dp.include_router(booking.router)
dp.include_router(cancel_booking.router)
dp.include_router(info.router)
dp.include_router(free_slots.router)
