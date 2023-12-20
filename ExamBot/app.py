from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from sql.delete import delete_cars
from sql.insert import insert_car, insert_user

from sql.select import select_car, select_user
from default_keyboards import main_menu, update_menu
from sql.update import update_name, update_photo
from states import AddCarState, DeleteCarState, RegisterState, UpdateState



token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    user = await select_user(chat_id=message.chat.id)
    if user:
        text = "Xush kelibsiz!"
        await message.answer(text=text, reply_markup=main_menu)
    else:
        text = "Assalomu alaykum! Ismingizni kiriting."
        await message.answer(text=text)
        await RegisterState.name.set()


@dp.message_handler(state=RegisterState.name)
async def get_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)

    text = "Telefon raqamingizni kiriting."
    await message.answer(text=text)
    await RegisterState.phone.set()


@dp.message_handler(state=RegisterState.phone)
async def get_phone_handler(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text, chat_id=message.chat.id)
    data = await state.get_data()

    await insert_user(data)

    text = "Siz ro'yxatdan o'tdingiz."
    await message.answer(text=text, reply_markup=main_menu)
    await state.finish()



# add_cars
@dp.message_handler(text="Add car")
async def add_car_handler(message: types.Message):
    text = "Mashina rasmini yuboring."
    await message.answer(text=text)
    await AddCarState.photo.set()


@dp.message_handler(state=AddCarState.photo, content_types=types.ContentType.PHOTO)
async def get_car_photo_handler(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)

    text = "Mashina nomini yuboring."
    await message.answer(text=text)
    await AddCarState.name.set()


@dp.message_handler(state=AddCarState.name)
async def car_name_handler(message: types.message, state: FSMContext):
    await state.update_data(name=message.text, chat_id=message.chat.id)
    text = "Mashina qo'shildi"
    await message.answer(text=text)
    data = await state.get_data()
    await insert_car(data)
    await state.finish()


#my cars
@dp.message_handler(text="My cars")
async def my_cats_handler(message: types.Message):
    cars = await select_car(chat_id=message.chat.id)
    for car in cars:
        caption = f"ID: {car[0]}\n\n NAME: {car[1]}"
        await message.answer_photo(photo=car[2], caption=caption)





# delete car

@dp.message_handler(text="Delete car")
async def delete_cat_handler(message: types.Message):
    text = "Mashina ID-sini kiriting."
    await message.answer(text=text)
    await DeleteCarState.id.set()


@dp.message_handler(state=DeleteCarState.id)
async def delete_cat(message: types.Message, state: FSMContext):
    if await delete_cars(int(message.text)):
        text = "Mashina muvaffaqiyatli o'chirildi!"
    else:
        text = "Noto'g'ri ID kiritdingiz."
    await message.answer(text=text, reply_markup=main_menu)
    await state.finish()


# update car

@dp.message_handler(text="Update car")
async def update_handler(message: types.Message):
    text = "Qaysi mashinani o'zgartimoqchisiz. ID sini kiriting."
    await message.answer(text=text)
    await UpdateState.id.set()


@dp.message_handler(state=UpdateState.id)
async def id_handler(message: types.Message, state: FSMContext):
    await state.update_data(id=int(message.text))
    text = "Qaysi ma'lumotni o'zgartirmoqchisiz."
    await message.answer(text=text, reply_markup=update_menu)
    await UpdateState.select.set()


@dp.message_handler(state=UpdateState.select)
async def select_handler(message: types.Message):
    column = message.text
    if column == "Photo":
        text = "Yangi rasmni kiriting"
        await message.answer(text=text)
        await UpdateState.photo.set()
    elif column == "Name":
        text = "Yangi nom kiriting"
        await message.answer(text=text)
        await UpdateState.name.set()



@dp.message_handler(state=UpdateState.photo, content_types=types.ContentType.PHOTO)
async def get_photo_handler(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    if await update_photo(data):
        text = "Rasm o'zgardi"
    else:
        text = "Botda muommo bor"
    await message.answer(text=text, reply_markup=main_menu)
    await state.finish()


@dp.message_handler(state=UpdateState.name)
async def get_name_handler(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    data = await state.get_data()
    if await update_name(data):
        text = "Nom ozgardi"
    else:
        text = "Botda muommo bor"
    await message.answer(text=text, reply_markup=main_menu)
    await state.finish()








if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)