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
phone_share = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Telefon raqamni jo'natish", request_contact=True)
    ]], resize_keyboard=True
)

location_share = ReplyKeyboardMarkup(
    keyboard=[[
        KeyboardButton(text="Manzilni jo'natish", request_contact=True)
    ]], resize_keyboard=True
)