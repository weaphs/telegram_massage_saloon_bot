from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from bot.keyboards.inline import main_menu_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message:Message):
    name = message.from_user.full_name
    await message.answer(f"Привіт! Вітаю Вас в массажному салоні 'Аврора'! Чим я можу Вам допомогти? ",
                         reply_markup= main_menu_keyboard())

@router.message(Command("info"))
async def cmd_info(message:Message):
    await message.answer("Наш салон знаходиться за адресою: м. Київ, вул. Героїв. Контактна особа: John Doe. "
                                  "Телефон +38097456278!", reply_markup=main_menu_keyboard())