# bot/handlers/cancel_booking
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, ForceReply
from db.models import Booking
from db import crud, database, models
from bot.handlers.start import cmd_start

router = Router()

@router.callback_query(F.data=="cancel_booking")
async def cmd_cancel(callback: CallbackQuery):
    user_id=callback.from_user.id
    async with database.async_session() as session:
        await crud.delete_bookings(session, user_id)
    await callback.message.answer("Всі Ваші записи видалено!")
    await cmd_start(callback.message)