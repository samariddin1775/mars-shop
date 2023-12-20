from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

user_main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Add Cars"),
        ],
        [
            KeyboardButton(text="Cars")
        ]
    ], resize_keyboard=True
)

update_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Photo"),
            KeyboardButton(text="Info"),
            KeyboardButton(text="Contact")
        ]
    ], resize_keyboard=True
)    