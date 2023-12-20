from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from default_keyboards import user_main_menu
from aiogram.dispatcher import FSMContext
from states import ContactState, AddproductState
from sql.insert import insert_product

token = "6020804140:AAGOUeaX322Rf0wivBNjAxVoCz9fjrVq5R4"
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    print(message)
    text = f"Assalomu alaykum, {message.from_user.full_name}"
    await message.answer(text=text, reply_markup=user_main_menu)


@dp.message_handler(text="Admin bilan aloqa")
async def contact_admin_handler(message: types.Message):
    text = "Iltimos, yubormoqchi bo'lgan habaringizni bitta habarda kiriting."
    await message.answer(text=text)
    await ContactState.text.set()


@dp.message_handler(state=ContactState.text)
async def get_contact_handler(message: types.Message, state: FSMContext):
    msg = message.text
    text = f"{message.from_user.full_name} ismli foydalanuvchi yangi habar yubordi: {msg}"
    await dp.bot.send_message(chat_id=1358470521, text=text)

    text1 = "Habar yuborildi ✅"
    await message.answer(text=text1)
    await state.finish()


@dp.message_handler(text="Mahsulot qo'shish")
async def add_product_handler(message: types.Message, state: FSMContext):
    text = "Iltimos, mahsulot rasmini kiriting"
    await message.answer(text=text)
    await AddproductState.image.set()



@dp.message_handler(state=AddproductState.image, content_types=types.ContentType.PHOTO)
async def get_image_handler(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    text = "Iltimos, mahsulot haqida ma'lumot kiriting."
    await message.answer(text=text)
    await AddproductState.info.set()


@dp.message_handler(state=AddproductState.info)
async def get_info_handler(message: types.Message, state: FSMContext):
    await state.update_data(info=message.text)
    text = "Iltimos, mahsulot narxini kiriting."
    await message.answer(text=text)
    await AddproductState.price.set()

   



@dp.message_handler(state=AddproductState.price)
async def get_price_handler(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    text = "Iltimos, aloqa uchun telefon raqam yoki telegram username kiriting."
    await message.answer(text=text)
    await AddproductState.contact.set()



@dp.message_handler(state=AddproductState.contact)
async def get_contact_handler(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    data = await state.get_data()
    image = data.get('image')
    info = data.get('info')
    contact = data.get('contact')
    price = data.get('price')


    await insert_product(data)

    photo = data.get('photo')
    info = data.get('info')
    contact = data.get('contact')
    price = data.get ('price')

    caption = f"Narxi: {price}\n{info}\n\n{contact}"
    await dp.bot.send_photo(chat_id=-1002140470690, photo=image, caption=caption)

    text = "Mahsulot gurpaga yuorildi."
    await message.answer(text=text)
    await state.finish()




if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)