from aiogram import Dispatcher, Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext

from default_keyboards import main_menu, phone_share, location_share
from states import RegisterState

token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    file = open('users.txt', 'r')
    users = file.read()
    if str(message.chat.id) in users:
        text = "Assalomu alaykum, xush kelibsiz."
        await message.answer(text=text, reply_markup=main_menu)
    else:
        text = "Assalomu alaykum, iltimos to'liq ismingizni kiriting"
        await RegisterState.full_name.set()
        await message.answer(text=text)

@dp.message_handler(text="Menu")
async def menu_handler(message: types.Message):
    text = 'jwjjwj'
    await message.answer(text=text, reply_markup=phone_share) 



# @dp.message_handler(text="Menu")
# async def menu_handler(message: types.Message):
#     photo = "https://hh-certificates.sgp1.digitaloceanspaces.com/blog/wp-content/uploads/2021/08/20142619/How-short-online-courses-can-actually-help-in-career.jpg"
#     caption = "Online kurs\nNarxi: 499 000 so'm"
#     await message.answer_photo(photo=photo, caption=caption,reply_markup=)     

@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Iltimos telefon raqamingizni kiriting."
    await message.answer(text=text, reply_markup=phone_share)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentType.CONTACT)
async def get_phone_number(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    text = "Iltimos manzilni kiriting."
    await message.answer(text=text, reply_markup=location_share)
    await RegisterState.location.set()


@dp.message_handler(state=RegisterState.location, content_types=types.ContentType.LOCATION)
async def get_location_handler(message: types.Message, state: FSMContext):
    await state.update_data(longitude=message.location.longitude, latitude=message.location.latitude)
    text = "Iltimos yoshingizni kiriting."
    await message.answer(text=text)
    await RegisterState.age.set()


@dp.message_handler(state=RegisterState.age)
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)

    data = await state.get_data()
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    age = data.get("age")
    longitude = data.get("longitude")
    latitude = data.get("latitude")
    text = f"""
Siz ro'yxatdan o'tdingiz.

{full_name}
{phone_number}
{age}
"""
    file = open('users.txt', 'a')
    file_text = f"{message.chat.id}&{full_name}&{phone_number}&{age}&{longitude}&{latitude}\n"
    file.write(file_text)
    await message.answer(text=text, reply_markup=main_menu)
    await state.finish()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
