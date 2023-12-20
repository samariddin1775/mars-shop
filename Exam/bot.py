from aiogram import Dispatcher, Bot, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from default_keyboards import register_menu
from inline_keyboards import mars_product

from states import RegisterState, FeedbackState

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

@dp.message_handler(text = "🪙 My coins")
async def get_full_name(message: types.Message):
    text = "Sizning Coiningiz 🪙750ta"
    await message.answer(text=text)

@dp.message_handler(text = "🎁 Products")
async def get_full_name(message: types.Message):
    text = "Product tanlang"
    await message.answer(text=text, reply_markup=mars_product)    

@dp.callback_query_handler(text="buy_airpods")
async def buy_strobar_handler(call: types.CallbackQuery):
    photo = "https://cdn.macbro.uz/macbro/36e8f416-f521-4677-8ff5-e0b9dc777558"
    caption = "Airpods - 559 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)  

@dp.callback_query_handler(text="buy_keyboards")
async def buy_keyboard_handler(call: types.CallbackQuery):
    photo = "https://m.media-amazon.com/images/I/71uCCuqkvxL.jpg"
    caption = "Keyboard - 350 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)             

@dp.callback_query_handler(text="buy_powerbank")
async def buy_strobar_handler(call: types.CallbackQuery):
    photo = "https://olcha.uz/image/266x266/products/OiVqM3FMFmQd6xRiTkyArQ4HQDbp3LHyT7P6Bh2GCiC3YzNl2QEPoxEyEBEc.jpg"
    caption = "Powerbank - 559 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)  

@dp.callback_query_handler(text="buy_watch")
async def buy_keyboard_handler(call: types.CallbackQuery):
    photo = "https://cdn.olcha.uz/image/400x400/products/woocomerce/sp-phone/2023-10-23/lyvJCW3ge42Snxp9uGfh5VNITQv62eZmHe5uvZVkfKj5tXM0gk42xRTF8ACrcSd6.jpeg"
    caption = "AppleWatch - 899 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)

@dp.callback_query_handler(text="buy_kb_sticker")
async def buy_strobar_handler(call: types.CallbackQuery):
    photo = "https://lzd-img-global.slatic.net/g/p/8259fa078450eb8332bf5aa48ee160f2.jpg_960x960q80.jpg_.webp"
    caption = "Keyboard Sticker - 29 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)  

@dp.callback_query_handler(text="buy_phone")
async def buy_keyboard_handler(call: types.CallbackQuery):
    photo = "https://olcha.uz/image/600x600/products/2021-04-13/xiaomi-mi-11-lite-5g-6-128gb-23185-0.jpeg"
    caption = "Phone - 3599 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)             

@dp.callback_query_handler(text="buy_earphone")
async def buy_strobar_handler(call: types.CallbackQuery):
    photo = "https://openshop.uz/public/storage/uploads/products/photos/202309/L9VGL98XoTF0MUtubpnTju3iu1svsaBuJe1P68Rw.jpg"
    caption = "Earphone - 459 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)  

@dp.callback_query_handler(text="buy_notebook")
async def buy_keyboard_handler(call: types.CallbackQuery):
    photo = "https://assets.manufactum.de/p/076/076768/76768_01.jpg/brunnen-notebook-kompagnon-128-x-95-cm.jpg?profile=pdsmain_1500"
    caption = "NoteBook - 200 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)


@dp.callback_query_handler(text="buy_sticker")
async def buy_strobar_handler(call: types.CallbackQuery):
    photo = "https://image.spreadshirtmedia.com/image-server/v1/mp/products/T1459A839PA3861PT28D1011204357W10000H10000/views/1,width=800,height=800,appearanceId=839,backgroundColor=F2F2F2/cartoon-planet-mars-sticker.jpg"
    caption = "Sticker - 70 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)  

@dp.callback_query_handler(text="buy_pen")
async def buy_keyboard_handler(call: types.CallbackQuery):
    photo = "https://m.media-amazon.com/images/I/81zuJI1P+UL.jpg"
    caption = "Pen - 25 coin🪙"
    await call.message.answer_photo(caption=caption, photo=photo)


@dp.message_handler(state=RegisterState.full_name)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    text = "Iltimos telefon raqamingizni kiriting."
    await message.answer(text=text)
    await RegisterState.phone_number.set()


@dp.message_handler(state=RegisterState.phone_number)
async def get_full_name(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.text)
    text = "Iltimos Modme ID kiriting."
    await message.answer(text=text)
    await RegisterState.modmeid.set()


@dp.message_handler(state=RegisterState.modmeid)
async def get_age(message: types.Message, state: FSMContext):
    await state.update_data(modmeid=message.text)
    text = "Password kiriting"
    await message.answer(text=text)
    await RegisterState.password.set()

@dp.message_handler(state=RegisterState.password)
async def get_location(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    


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
    file_text = f"{message.chat.id}&{full_name}&{phone_number}&{modmeid}&{password}\n"
    file.write(file_text)
    await message.answer(text=text)
    await state.finish()


@dp.message_handler(text="✍️ Fikr bildirish")
async def feedback_handler(message: types.Message):
    photo = "https://storum.ru/catalog/view/theme/storum_3/image/information/reviews/top-banner-main.png"
    text = "✍️ Fikr qoldirish"
    await message.answer_photo(caption=text, photo=photo)
    await FeedbackState.feedback.set()


@dp.message_handler(state=FeedbackState.feedback)
async def feedback_get_handler(message: types.Message, state: FSMContext):
    user = await user(message.chat.id)
    user += f"\n{message.text}"
    await dp.bot.send_message(chat_id=5744360920, text=user)
    text = "Habar yuborildi ✔️"
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
            text = f"Name👤 : {user[1]}\n Phone📱 : {user[2]}\n Modme ID🆔 :{user[3]}\n Password🔒  : {user[4]}\n "
            print(text)
    await message.answer(text=text)    

    
        


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)