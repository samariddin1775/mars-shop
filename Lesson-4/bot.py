from aiogram import Dispatcher, executor, Bot, types

from keyboards import main_menu, fruits_menu, t_shirts_menu, vegetables_menu, wears_menu, shoes_menu

token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
bot = Bot(token=token)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Assalomu alaykum, hurmatli mehmon"
    await message.answer(text=text, reply_markup=main_menu)


@dp.message_handler(text="Mevalar")
async def mavalar_handler(message: types.Message):
    text = "Bu mevalar juda  ham mazali"
    await message.answer(text=text, reply_markup=fruits_menu)

@dp.message_handler(text="Futbolkalar")
async def mavalar_handler(message: types.Message):
    text = "Bu mevalar juda  ham mazali"
    await message.answer(text=text, reply_markup=t_shirts_menu)


@dp.message_handler(text="Sabzavotlar")
async def mavalar_handler(message: types.Message):
    text = "Bu mevalar juda  ham mazali"
    await message.answer(text=text, reply_markup=vegetables_menu) 

@dp.message_handler(text="Kiyimlar")
async def mavalar_handler(message: types.Message):
    text = "Bu mevalar juda  ham mazali"
    await message.answer(text=text, reply_markup=wears_menu) 

@dp.message_handler(text="Oyoq kyimlar")
async def mavalar_handler(message: types.Message):
    text = "Bu mevalar juda  ham mazali"
    await message.answer(text=text, reply_markup=shoes_menu) 


    
@dp.message_handler(text="Mashinalar")
async def mavalar_handler(message: types.Message):
    text = "Bu mevalar juda  ham mazali"
    await message.answer(text=text)  





@dp.message_handler(text="Back")
async def mavalar_handler(message: types.Message):
    text = "Bu mevalar juda  ham mazali"
    await message.answer(text=text, reply_markup=main_menu)     
              


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)