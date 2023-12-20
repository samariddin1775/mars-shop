from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

mars_product = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Mars Airpods", callback_data="buy_airpods"),
            InlineKeyboardButton(text="Mars Keyboard", callback_data="buy_keyboards")
        ],
        [
            InlineKeyboardButton(text="Mars Powerbank", callback_data="buy_powerbank"),
            InlineKeyboardButton(text="Mars Watch", callback_data="buy_watch")
        ],
        [
            InlineKeyboardButton(text="Keyboard Sticker", callback_data="buy_kb_sticker"),
            InlineKeyboardButton(text="Mars Phone", callback_data="buy_phone")
        ],
        [
            InlineKeyboardButton(text="Mars Earphones", callback_data="buy_earphone"),
            InlineKeyboardButton(text="Mars Notebook", callback_data="buy_notebook")
        ],
        [
            InlineKeyboardButton(text="Mars Sticker", callback_data="buy_sticker"),
            InlineKeyboardButton(text="Mars Pen", callback_data="buy_pen")
        ]
    ]
)
