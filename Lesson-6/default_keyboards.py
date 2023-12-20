from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from default_keyboards import back

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asosiy menu", callback_data="mainmenu"),
            
        ]

    ], resize_keyboard=True
) 