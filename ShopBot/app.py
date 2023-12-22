from aiogram import Dispatcher, executor, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from default_keyboards import KeyboardButton, ReplyKeyboardMarkup, shop_main_menu
from environs import Env


env = Env()
env.read_env()


BOT_TOKEN = env.str("TOKEN")

storage = MemoryStorage()
bot = Bot(token=BOT_TOKEN, proxy="https://proxy.server:3128" )
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Assalomu alaykum, hurmatli mehmon"
    await message.answer(text=text, reply_markup=shop_main_menu)





if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)