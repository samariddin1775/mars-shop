from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



calculator_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hisoblash"),
            
        ]

    ], resize_keyboard=True
) 

# hisoblash = ReplyKeyboardMarkup(
#     keyboard=[
#         [
#             KeyboardButton(text='Plus'),
#             KeyboardButton(text= 'Minus'),
#         ],
#         [
#             KeyboardButton(text='Kopaytirish'),
#             KeyboardButton(text= 'Bolish'),
#         ],
#     ], resize_keyboard=True
# )