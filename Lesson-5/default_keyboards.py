from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            
            KeyboardButton(text="Menu"),
        ],
        [
            KeyboardButton(text="My orders"),
        ],
        [
            KeyboardButton(text="Review"),
            KeyboardButton(text="Settings"),
        ],
    ], resize_keyboard=True
)

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Lavash"),
            KeyboardButton(text="Gamburger")
        ],
        [
            KeyboardButton(text="Hot-Dog"),
            KeyboardButton(text="Sandwich")
        ],
        [
            KeyboardButton(text="Subway"),
            KeyboardButton(text="Back")
        ]
         
    ], resize_keyboard=True
) 