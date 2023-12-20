from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

lavash_buy = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Sotib olish", callback_data="buy_lavash")
        ]
    ]
)

# sticker_buy = InlineKeyboardMarkup(
#     inline_keyboard=[

#         [
#             InlineKeyboardButton(text="Sotib olish", callback_data="buy_sticker")
#         ]

#     ]
# )

# blacknote_buy = InlineKeyboardMarkup(
#     inline_keyboard=[

#         [
#             InlineKeyboardButton(text="Sotib olish", callback_data="buy_blacknote")
#         ]

#     ]
# )