# db/crud.py
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, and_, delete
from typing import Optional, List
from datetime import datetime, date
from .models import Booking
from utils.time_slots import generate_free_slots
from bot.scheduler.notify import remove_notification

# -------------------------------
# BOOKING
# -------------------------------
async def is_slot_free(db: AsyncSession, date: datetime.date, time: datetime.time) -> bool:
    result = await db.execute(
        select(Booking).where(
            and_(Booking.book_date == date, Booking.book_time == time,  Booking.status == "free")
        )
    )
    return result.scalar_one_or_none() is None


async def create_booking(db: AsyncSession, user_id: int, name: str, date: datetime.date, time: datetime.time) -> Booking:
    booking = Booking(user_id=user_id, book_date=date, name=name, book_time = time, status="booked")
    db.add(booking)
    await db.commit()
    await db.refresh(booking)
    return booking
# -------------------------------
# DELETE BOOKING
# -------------------------------

async def delete_bookings(db: AsyncSession, user_id: int) -> int:
    bookings = await db.execute(select(Booking).where(Booking.user_id == user_id))
    bookings = bookings.scalars().all()
    for booking in bookings:
        remove_notification(user_id, booking.id)

    result = await db.execute(
        delete(Booking).where(Booking.user_id == user_id)
    )
    await db.commit()
    return result.rowcount or 0

# -------------------------------
# FREE SLOTS
# -------------------------------


async def get_free_slots(db: AsyncSession, day: date)-> Optional[List[str]]:
    all_slots = generate_free_slots(day)
    result = await db.execute(
        select(Booking.book_time).where(Booking.book_date == day, Booking.status == "booked")
    )
    booked = [t.strftime("%H:%M") for t in result.scalars().all()]

    return [s for s in all_slots if s not in booked]



