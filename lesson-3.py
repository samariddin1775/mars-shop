import requests
from aiogram import Bot, Dispatcher, executor, types

token = "6434315395:AAFRvc7Kznok_iG2RyGEnBxJ7CnXUn034Hw"

bot = Bot(token=token)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands="start")
async def start_handler(message: types.Message):
    text = "Assalomu alaykum"
    await message.answer(text=text)


# @dp.message_handler(commands="all")
# async def all_currency_handler(message: types.Message):
#     response = requests.get("https://nbu.uz/uz/exchange-rates/json/").json()
#     text = ""
#     for i in response:
#         text += f"{i['title']} | {i['cb_price']}\n"
#     await message.answer(text=text)

@dp.message_handler(commands="duck")
async def duck_image(message: types.Message):
    response = requests.get('https://random-d.uk/api/random').json() 
    await message.answer_photo(photo = response['url'])


# @dp.message_handler()
# async def find_currency(message: types.Message):
#     code = message.text.split()[0]
#     price = float(message.text.split()[1])
#     response = requests.get("https://nbu.uz/uz/exchange-rates/json/").json()
#     for cur in response:
#         if cur['code'] == code:
#             total = float(cur['cb_price']) * price
#             text = f"1 {code} == {cur['cb_price']} so'm\n{price} {code} == {total} so'm"
#             await message.answer(text=text)
#             break


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)