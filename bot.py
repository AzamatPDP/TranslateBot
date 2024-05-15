from googletrans import Translator
from aiogram import executor, types, Bot, Dispatcher
import logging

API_TOKEN = '7181183321:AAHeWHRD1eaiX69IC8WOp8ozJGsUdR2Q3wI'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

translator = Translator()

@dp.message_handler(commands=["start", "help"])
async def hello(message: types.Message):
    await message.answer("Assalomu aleykum botimizga xush kelibsiz!\nMatningizni yuboring")

@dp.message_handler()
async def get_data(message: types.Message):
    translation = translator.translate(message.text, dest='en')
    translated_text = translation.text
    await message.reply(translated_text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)