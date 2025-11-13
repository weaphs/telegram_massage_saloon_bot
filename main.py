#main.py
import asyncio
import logging
import sys
from os import getenv
from bot.bot import bot, dp
from bot.scheduler.notify import start_scheduler

async def main():
    start_scheduler()
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
