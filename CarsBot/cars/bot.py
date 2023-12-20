from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from default_keyboards import user_main_menu, update_menu
from aiogram.dispatcher import FSMContext
from states import ContactState, AddproductState, UpdateState
from sql.insert import insert_product

token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
storage = MemoryStorage()
bot = Bot(token=token)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    print(message)
    text = f"Assalomu alaykum, {message.from_user.full_name}"
    await message.answer(text=text)



@dp.message_handler(commands="cars")
async def start_handler(message: types.Message):
    print(message)
    text = "Tanlang"
    await message.answer(text=text, reply_markup=user_main_menu)    


@dp.message_handler(text="Mahsulot qo'shish")
async def add_product_handler(message: types.Message, state: FSMContext):
    text = "Iltimos, mahsulot rasmini kiriting"
    await message.answer(text=text)
    await AddproductState.image.set()



@dp.message_handler(state=AddproductState.image, content_types=types.ContentType.PHOTO)
async def get_image_handler(message: types.Message, state: FSMContext):
    await state.update_data(image=message.photo[-1].file_id)
    text = "Iltimos, mahsulot nomini kiriting"
    await message.answer(text=text)
    await AddproductState.name.set()


# @dp.message_handler(state=AddproductState.info)
# async def get_info_handler(message: types.Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await AddproductState.price.set() 




@dp.message_handler(state=AddproductState.name)
async def get_contact_handler(message: types.Message, state: FSMContext):
    await state.update_data(contact=message.text)
    data = await state.get_data()
    image = data.get('image')
    name = data.get('name')
    
    await insert_product(data)
    await state.finish()




@dp.message_handler(commands="qwerty")
async def update_handler(message: types.Message):
    text = "Qaysi mahsulotni o'zgartimoqchisan. ID sini kirit."
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
    if column == "Rasm":
        text = "Yangi rasmni kiriting"
        await message.answer(text=text)
        await UpdateState.photo.set()
    elif column == "Info":
        text = "Yangi malumot kiriting"
        await message.answer(text=text)
        await UpdateState.info.set()


@dp.message_handler(state=UpdateState.photo, content_types=types.ContentType.PHOTO)
async def get_photo_handler(message: types.Message, state: FSMContext):
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    if await update_photo(data):
        text = "Rasm o'zgardi"
    else:
        text = "Botda muommo bor"
    await message.answer(text=text, reply_markup=user_main_menu)
    await state.finish()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)       