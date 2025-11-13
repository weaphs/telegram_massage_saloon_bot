#bot/handlers/booking.py
from aiogram import Router, F
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from bot.fsm.free_slots import Free_slot_states
from aiogram.types import Message, CallbackQuery, ForceReply
from bot.keyboards.inline import main_menu_keyboard
from datetime import datetime
from db import crud, database, models
from bot.handlers.start import cmd_start

router = Router()

@router.callback_query(F.data == 'free_slots', StateFilter(None))
async def ent_name(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer("Введіть дату яка вас цікавить! "
                                  "Формат вводу: YYYY-MM-DD", reply_markup=ForceReply(input_field_placeholder="YYYY-MM-DD"))
    await state.set_state(Free_slot_states.entering_date)

@router.message(Free_slot_states.entering_date)
async def ent_date(message: Message, state: FSMContext):
    try:
        date_obj = datetime.strptime(message.text, "%Y-%m-%d").date()
    except ValueError:
        await message.answer("Невірний формат дати. Використай формат YYYY-MM-DD.")
        return

    async with database.async_session() as session:
        slots = await crud.get_free_slots(session,date_obj)

        if not slots:
            await message.answer("На дану дату вільних місць немає!", reply_markup= main_menu_keyboard())

        else:
            free_list = "\n".join(f"🕒 {s}" for s in slots)
            await  message.answer(f"Вільні місця на {date_obj}:\n\n{free_list}",
                           reply_markup=main_menu_keyboard())

    await state.clear()



