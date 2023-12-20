from aiogram import types, Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from default_keyboards import start_test
from utils import make_keyboards

quiz_list = [
    {
        "id": 1,
        "savol": "Python nechinchi yil ixtiro qilingan",
        "javoblar": {
            "A": 1991,
            "B": 1993,
            "C": 1995,
            "D": 1996,
        },
        "t_javob": "A"
    },
    {
        "id": 2,
        "savol": "Python nechta malumot turi bor",
        "javoblar": {
            "A": 1,
            "B": 2,
            "C": 4,
            "D": 9,
        },
        "t_javob": "D"
    },
    {
        "id": 3,
        "savol": "Yahyobek nechchi yoshda",
        "javoblar": {
            "A": 20,
            "B": 18,
            "C": 16,
            "D": 10,
        },
        "t_javob": "D"
    }
]

answers = list()


token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Salom, testni boshlash uchun pastdagi tugmadan foydalaning."
    await message.answer(text, reply_markup=start_test)


@dp.message_handler(text="Testni boshlash 🚀")
async def start_test_handler(message: types.Message, state: FSMContext):
    await state.update_data(test_id=1)
    text, markup = await make_keyboards(1, quiz_list)
    await message.answer(text=text, reply_markup=markup)
    await state.set_state("test-answer")


@dp.message_handler(state="test-answer", text="Javoblarni ko'rish 👀")
async def get_answer_handler(message: types.Message, state: FSMContext):
    text = ""
    for ans in answers.items():
        text += f"{ans[0]} | {ans[1]}\n"
    await message.answer(text=text, reply_markup=start_test)
    await state.finish()


@dp.message_handler(state="test-answer")
async def get_user_answer_handler(message: types.Message, state: FSMContext):
    data = await state.get_data()
    test_id = int(data.get("test_id"))
    answers[test_id] = message.text
    await state.update_data(test_id=test_id + 1)
    text, markup = await make_keyboards(test_id=test_id + 1, quiz_list=quiz_list)
    await message.answer(text=text, reply_markup=markup)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)