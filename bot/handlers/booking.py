#bot/handlers/booking.py
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from bot.fsm.booking import BookingStates
from aiogram.types import Message, CallbackQuery, ForceReply
from bot.keyboards.inline import main_menu_keyboard
from datetime import datetime, timedelta
from db import crud, database, models
from bot.handlers.start import cmd_start
from bot.scheduler.notify import schedule_notification
router = Router()

@router.callback_query(F.data == 'booking', StateFilter(None))
async def ent_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введіть своє повне ім'я!")
    await state.set_state(BookingStates.entering_name)

@router.message(BookingStates.entering_name)
async def ent_date(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer("Введіть дату запису! "
                         "Формат вводу: YYYY-MM-DD", reply_markup=ForceReply(input_field_placeholder="YYYY-MM-DD"))
    await state.set_state(BookingStates.entering_date)

@router.message(BookingStates.entering_date)
async def ent_time(message: Message, state: FSMContext):
    await state.update_data(date=message.text)
    await message.answer("Введіть час запису! "
                         "Формат вводу: HH:MM", reply_markup=ForceReply(input_field_placeholder="HH:MM"))
    await state.set_state(BookingStates.entering_time)

@router.message(BookingStates.entering_time)
async def conform(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    data = await state.get_data()
    name_str = data["name"]
    date_str = data["date"]
    time_str = data["time"]
    user_id = message.from_user.id
    booking_id:int=0
    try:
        book_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        book_time = datetime.strptime(time_str, "%H:%M").time()
    except ValueError:
        await message.answer("Невірний формат дати або часу. Спробуй ще раз.")
        return
    async with database.async_session() as session:
        if await crud.is_slot_free(session, book_date, book_time):
            result = await crud.create_booking(session, user_id, name_str, book_date, book_time)
            booking_id = result.id
    await message.answer(f"Дякую {name_str}, Ви записані {date_str} на {time_str}")

    #REMINDING WITH APSHCEDULER
    booking_dt = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
    notify_time = booking_dt - timedelta(hours=1)  # нагадати за 1 годину
    text = f"🔔 Привіт, {name_str}! Нагадуємо, що Ваш запис о {time_str} ({date_str})."

    # створюємо задачу в APScheduler
    schedule_notification(message.bot,message.from_user.id,booking_id,  notify_time, text)
    await state.clear()
    await cmd_start(message)