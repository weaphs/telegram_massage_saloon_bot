# bot/keyboards/inline.py
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def main_menu_keyboard ():
    buttons = [
        [InlineKeyboardButton(text="Зробити запис", callback_data="booking")],
        [InlineKeyboardButton(text="Подивитись вільні місця", callback_data="free_slots")],
        [InlineKeyboardButton(text="Про нас",callback_data="info")],
        [InlineKeyboardButton(text="Скасувати запис", callback_data="cancel_booking")]
    ]
    main_menu_keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    return main_menu_keyboard