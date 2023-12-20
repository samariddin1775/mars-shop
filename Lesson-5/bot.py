# from aiogram import Dispatcher, executor, Bot, types

# from default_keyboards import main_menu, menu

# from inline_keyboards import lavash_buy
# # from inline_keyboards import sticker_buy



# token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"
# bot = Bot(token=token)
# dp = Dispatcher(bot)


# @dp.message_handler(commands="start")
# async def start_handler(message: types.Message):
#     text = "Assalomu alaykum, hurmatli mehmon"
#     await message.answer(text=text, reply_markup=main_menu)


# @dp.message_handler(text="Menu")
# async def strobar_handler(message: types.Message):
#     text= 'Menyudan xohlagan narsangizni tanlang'
    
#     await message.answer(text=text,reply_markup=menu)

# @dp.message_handler(text="Lavash")
# async def strobar_handler(message: types.Message):
#     photo = "https://pasta.uz/upload/products/%D0%9B%D0%B0%D0%B2%D0%B0%D1%88.jpg"
#     caption = "Juda mazali lavash \nNarxi: 29 000 so'm"
#     await message.answer_photo(photo=photo, caption=caption, reply_markup=lavash_buy) 



# @dp.callback_query_handler(text="buy_lavash")
# async def buy_strobar_handler(call: types.CallbackQuery):
#     text = "Lavash sotib oldingiz."
#     await call.message.answer(text=text)





# @dp.message_handler(text="My orders")
# async def strobar_handler(message: types.Message):
#     photo = "https://lab.marsit.uz/media/shop/MARS sticker/mars-sticker.jpeg"
#     caption = "Mars juda zor sticker \nCoins: 75"
#     await message.answer_photo(photo=photo, caption=caption) 


# @dp.message_handler(text="Back")
# async def mavalar_handler(message: types.Message):
#     text = "Siz bosh menyudasiz"
#     await message.answer(text=text, reply_markup=main_menu)   



# @dp.callback_query_handler(text="buy_sticker")
# async def buy_strobar_handler(call: types.CallbackQuery):
#     text = "Mars Sticker sotib oldingiz. Bu sizning maxsus raqamingiz. 12123"
#     await call.message.answer(text=text)       






# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)