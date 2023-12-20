from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



register_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍️ Registration"),
            KeyboardButton(text="👤 Profile"),
        ],
        [
            KeyboardButton(text="Kurslar"),
        ]
        
    ], resize_keyboard=True
) 

kurslar_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Kurslar haqida malumot olish."),
        ],
        [
            KeyboardButton(text="Kurs qoshish"),
        ],
        [
            KeyboardButton(text="Back"),
        ]
    ], resize_keyboard=True


)


