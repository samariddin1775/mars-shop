from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Add car"),
            KeyboardButton(text="My cars")
        ],
        [
            KeyboardButton(text="Delete car"),
            KeyboardButton(text="Update car")
        ]
    ], resize_keyboard=True
)


update_menu = ReplyKeyboardMarkup(
    keyboard=[

        [
            KeyboardButton(text="Photo"),
            KeyboardButton(text="Name")
        ]
    ], resize_keyboard=True
)