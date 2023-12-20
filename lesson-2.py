# from aiogram import Bot, Dispatcher, executor, types
# import wikipedia
# import logging

# bot = Bot(token='6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw')
# dp = Dispatcher(bot)

# logging.basicConfig(level=logging.INFO)


# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     ism = message.from_user.first_name
#     await message.answer(f"Salom {ism}")


# @dp.message_handler()
# async def echo_bot(message: types.Message):
#     try:
#         wikipedia.set_lang("uz")
#         a = wikipedia.summary(message.text)
#         await message.answer(a)
#     except:
#         await message.reply("Itimos to'g'ri ma'lumot kiriting.")


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)



# from aiogram import Bot, Dispatcher, executor, types
# import logging
# import requests


# bot = Bot(token='6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw')
# dp = Dispatcher(bot)

# url = 'https://v6.exchangerate-api.com/v6/afff1a78fcb6779e4e7b563e/pair/USD/UZS'
# sayt = requests.get(url).json()
# natija = (sayt['conversion_rate'])

# logging.basicConfig(level=logging.INFO)


# @dp.message_handler(commands=['start'])
# async def start(message: types.Message):
#     ism = message.from_user.first_name
#     await message.answer(f"Salom {ism} bungi kunda 1 USD {natija} so'mga teng.")


# if __name__ == '__main__':
#     executor.start_polling(dp, skip_updates=True)


