#bot/scheduler/notify.py
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from config.settings import settings


jobstores = {"default": SQLAlchemyJobStore(url=settings.SYNC_DATABASE_URL)}
scheduler = AsyncIOScheduler(jobstores=jobstores)


def start_scheduler():
    scheduler.start()

async def send_notification(bot: Bot, user_id: int, text: str):
    try:
        await bot.send_message(user_id, text)
    except Exception as e:
        print(f"❌ Помилка при відправці нагадування: {e}")

async def scheduled_job(bot_token: str, user_id: int, text: str):
    bot = Bot(token=bot_token)
    await send_notification(bot, user_id, text)
    await bot.session.close()

def schedule_notification(bot: Bot, user_id: int, booking_id:int, notify_time: datetime, text: str):
    scheduler.add_job(
        scheduled_job,
        trigger="date",
        run_date=notify_time,
        args=[bot.token, user_id, text],
        id=f"notify_{user_id}_{booking_id}",
        replace_existing=True,
    )


def remove_notification(user_id: int, booking_id: int ):
    job_id = f"notify_{user_id}_{booking_id}"

    job = scheduler.get_job(job_id)
    if job:
        scheduler.remove_job(job_id)
        print(f"🗑 Видалено нагадування {job_id}")
    else:
        print(f"⚠️ Немає job з id={job_id}")