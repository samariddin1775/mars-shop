from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main_menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="buy"),
            
        ], 
        [
            InlineKeyboardButton(text = "ℹ Biz haqimizda", callback_data="about_us"),
            InlineKeyboardButton(text = "🛍 Buyurtmalarim", callback_data="orders"),
        ],
        [
            InlineKeyboardButton(text ="🏘 Filiallar", callback_data="branches"),
        
        ],
        [
            InlineKeyboardButton(text="✍️ Fikr bildirish", callback_data="opinion"),
            InlineKeyboardButton(text="⚙️ Sozlamalar", callback_data="settings"),
        ]

    ],
)