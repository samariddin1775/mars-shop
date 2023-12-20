from aiogram import Dispatcher, executor, Bot, types

from default_keyboards import KeyboardButton, ReplyKeyboardMarkup, shop_main_menu


token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Assalomu alaykum, hurmatli mehmon"
    await message.answer(text=text, reply_markup=shop_main_menu)



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)