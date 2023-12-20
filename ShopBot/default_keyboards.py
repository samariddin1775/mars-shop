from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

shop_main_menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text="Shop"),
            KeyboardButton(text="Add product")
        ]
    ], resize_keyboard=True 
)