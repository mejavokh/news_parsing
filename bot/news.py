from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import json

from aiogram.types import ParseMode

token = '7126703168:AAF5lvyDWcsOMjzMueS9oMWS9dphSQ_HNgg'
bot = Bot(token=token)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Salom! So`nggi yangiliklarni ko`rish uchun /list ni bosing')


@dp.message_handler(commands=['list'])
async def list_news(message: types.Message):
    with open('date/all_articles_dict.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    response = ''
    for item in data:
        response += f"<b>{item['title'].strip()}</b>\n{item['description']}\n\n"

    await message.reply(response, parse_mode=ParseMode.HTML)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)





