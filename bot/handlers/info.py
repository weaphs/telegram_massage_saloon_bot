# bot/handlers/info
from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from bot.keyboards.inline import main_menu_keyboard


router = Router()

@router.callback_query(F.data=="info")
async def cmd_cancel(callback: CallbackQuery):
    await callback.message.answer("Наш салон знаходиться за адресою: м. Київ, вул. Героїв. Контактна особа: John Doe. "
                                  "Телефон +38097456278!", reply_markup= main_menu_keyboard())
