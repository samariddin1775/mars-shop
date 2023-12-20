from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


async def make_keyboards(test_id, quiz_list):
    for test in quiz_list:
        if test_id in test.values():
            text = test['savol']
            markup = ReplyKeyboardMarkup(
                keyboard=[
                    [
                        KeyboardButton(text=test['javoblar']['A']),
                        KeyboardButton(text=test['javoblar']['B'])
                    ],
                    [
                        KeyboardButton(text=test['javoblar']['C']),
                        KeyboardButton(text=test['javoblar']['D'])
                    ]
                ], resize_keyboard=True
            )
            return text, markup
    text = "Javoblarni ko'rish"
    markup = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Javoblarni ko'rish 👀")
        ]], resize_keyboard=True
    )
    return text, markup