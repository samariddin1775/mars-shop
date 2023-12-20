from aiogram import Dispatcher, Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from default_keyboard import register_menu, kurslar_menu

from states import RegisterState

token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    file = open('user.txt', 'r')
    users = file.read()
    if str(message.chat.id) in users:
        text = "Assalomu alaykum, xush kelibsiz."
    else:
        text = "Assalomu alaykum, iltimos to'liq ismingizni kiriting"
        await RegisterState.full_name.set()
    await message.answer(text=text, reply_markup=register_menu)

@dp.message_handler(text="Back")
async def mavalar_handler(message: types.Message):
    text = "Siz bosh menyudasiz"
    await message.answer(text=text, reply_markup=register_menu) 


# @dp.message_handler(text="")
# async def strobar_handler(message: types.Message):
#     photo = "https://hh-certificates.sgp1.digitaloceanspaces.com/blog/wp-content/uploads/2021/08/20142619/How-short-online-courses-can-actually-help-in-career.jpg"
#     caption = "Online kurs\nNarxi: 29 000 so'm"
#     await message.answer_photo(photo=photo, caption=caption) 


@dp.message_handler(text="Kurslar")
async def strobar_handler(message: types.Message):
    text= 'Siz bosh menyudasiz'
    
    await message.answer(text=text,reply_markup=kurslar_menu)       


@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Iltimos telefon raqamingizni kiriting."
    await message.answer(text=text)
    await RegisterState.phone_number.set()



    text = "Iltimos yoshingizni kiriting."
    await message.answer(text=text)
    await RegisterState.modmeid.set()


@dp.message_handler(state=RegisterState.modmeid)
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    text = "Qaysi viloyata yoki shaharda yashiysiz"
    await message.answer(text=text)
    await RegisterState.password.set()

@dp.message_handler(state=RegisterState.password)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(location=message.text)
    


    data = await state.get_data()
    full_name = data.get("full_name")
    phone_number = data.get("phone_number")
    modmeid = data.get("modmeid")
    password = data.get("password")
    
    text = f"""
Siz ro'yxatdan o'tdingiz.

{full_name}
{phone_number}
{modmeid}
{password}

"""
    file = open('user.txt', 'a')
    file_text = f"{message.chat.id}&{full_name}&{phone_number}&{age}&{location}&{school}\n"
    file.write(file_text)
    await message.answer(text=text)
    await state.finish()



@dp.message_handler(text="👤 Profile")
async def profile_handler(message: types.Message):
    file = open('user.txt', 'r')
    users = file.readlines()
    text = "Siz hali ro'yxatdan o'tmadingiz."
    for line in users:
        user = line.split("&")      
        if user[0] == str(message.chat.id):
            text = f"👤 : {user[1]}\n 📱: {user[2]}\n 📊:{user[3]}\n 🏘: {user[4]}\n 🏫:{user[5]}\n"
            print(text)
    await message.answer(text=text)    

    
        


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)