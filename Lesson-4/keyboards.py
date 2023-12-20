from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Mevalar"),
            KeyboardButton(text="Futbolkalar")
        ],
        [
            KeyboardButton(text="Sabzavotlar"),
            KeyboardButton(text="Kiyimlar")
        ],
        [
            KeyboardButton(text="Oyoq kiyimlar"),
            KeyboardButton(text="Mashinalar")
        ]
         
    ], resize_keyboard=True
) 


fruits_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Apple"),
            KeyboardButton(text="Banana")
        ],
        [
            KeyboardButton(text="Cherry"),
            KeyboardButton(text="Limon")
        ],
        [
            KeyboardButton(text="Pineapple"),
            KeyboardButton(text="Back")
        ]
         
    ], resize_keyboard=True
) 
t_shirts_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Nike-T-Shirt"),
            KeyboardButton(text="Adidas-T-Shirt")
        ],
        [
            KeyboardButton(text="Puma-T-Shirt"),
            KeyboardButton(text="Polo-T-Shirt")
        ],
        [
            KeyboardButton(text="New Balance-T-Shirt"),
            KeyboardButton(text="Back")
        ]
         
    ], resize_keyboard=True
) 

vegetables_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Potato"),
            KeyboardButton(text="Tomato")
        ],
        [
            KeyboardButton(text="Onion"),
            KeyboardButton(text="Carrot")
        ],
        [
            KeyboardButton(text="Rediska"),
            KeyboardButton(text="Back")
        ]
         
    ], resize_keyboard=True
) 

wears_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="T-Shirt"),
            KeyboardButton(text="Jeans")
        ],
        [
            KeyboardButton(text="Cap"),
            KeyboardButton(text="Shoes")
        ],
        [
            KeyboardButton(text="Shorts"),
            KeyboardButton(text="Back")
        ]
         
    ], resize_keyboard=True
) 

shoes_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Nike"),
            KeyboardButton(text="Adidas")
        ],
        [
            KeyboardButton(text="Puma"),
            KeyboardButton(text="Polo")
        ],
        [
            KeyboardButton(text="New Balance"),
            KeyboardButton(text="Back")
        ]
         
    ], resize_keyboard=True
) 