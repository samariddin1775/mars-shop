from aiogram import Dispatcher, executor, Bot, types

from default_keyboards import  mainmenu
from inline_keyboards import main_menu


token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"

bot = Bot(token=token)

dp = Dispatcher(bot)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Assalomu alaykum, hurmatli mehmon"
    await message.answer(text=text, reply_markup=mainmenu)

    text2 = "jhgfdfgh"


@dp.message_handler(text="Menu")
async def strobar_handler(message: types.Message):
    text= "Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin Oqtepa Lavash menu "
    photo ="https://telegra.ph/Taomnoma-09-30"
    await message.answer_photo(photo=photo, text=text, reply_markup=main_menu)









if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)