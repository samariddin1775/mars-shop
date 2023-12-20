from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



register_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="✍️ Fikr bildirish"),
            KeyboardButton(text="👤 Profile"),
        ],
        [
            KeyboardButton(text="🪙 My coins"),
             KeyboardButton(text="🎁 Products"),
        ]
        
    ], resize_keyboard=True
) 




