from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mahsulot qo'shish"),
            KeyboardButton(text="Mening mahsulotlarim")
        ],
        [
            KeyboardButton(text="Admin bilan aloqa")
        ]
    ], resize_keyboard=True
)