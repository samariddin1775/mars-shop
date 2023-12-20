from aiogram import Dispatcher, executor, Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from default_keyboards import calculator_menu
from state import CalculatorState

token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Assalomu alaykum"
    await message.answer(text=text, reply_markup=calculator_menu)


@dp.message_handler(text="➖ Hisoblash ➕")
async def calculator(message: types.Message):
    text = "Birinchi sonni kiriting..."
    await message.answer(text=text)
    await CalculatorState.num1.set()


@dp.message_handler(state=CalculatorState.num1)
async def calculator(message: types.Message, state: FSMContext):
    await state.update_data(num1=message.text)
    text = "Ikkinchi sonni kiriting..."
    await message.answer(text=text)
    await CalculatorState.num2.set()


@dp.message_handler(state=CalculatorState.num2)
async def calculator(message: types.Message, state: FSMContext):
    await state.update_data(num2=message.text)
    text = "Hisoblash uchun belgini kiriting..."
    await message.answer(text=text)
    await CalculatorState.sign.set()


@dp.message_handler(state=CalculatorState.sign)
async def calculator(message: types.Message, state: FSMContext):
    await state.update_data(sign=message.text)

    data = await state.get_data()
    num1 = int(data.get("num1"))
    num2 = int(data.get("num2"))
    sign = data.get("sign")

    text = ""
    if sign == "+":
        text = f"{num1} + {num2} = {num1 + num2}"
    elif sign == "-":
        text = f"{num1} - {num2} = {num1 - num2}"
    elif sign == "/":
        text = f"{num1} / {num2} = {num1 / num2}"
    elif sign == "*":
        text = f"{num1} * {num2} = {num1 * num2}"
    await message.answer(text=text, reply_markup=calculator_menu)
    await state.finish()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)