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
    await message.answer("Assalomu aleykum botimizga xush kelibsiz!\nEnglish va Uzbek tilidagi matningizni yuboring")


@dp.message_handler()
async def get_data(message: types.Message):
    # Foydalanuvchining matnini aniqlash
    user_language = translator.detect(message.text).lang

    # Agar foydalanuvchi ingliz tilida yozgan bo'lsa, o'zbek tiliga tarjima qilish
    if user_language == 'en':
        translation = translator.translate(message.text, dest='uz')
        await message.reply(f"Uzbekcha: {translation.text}")
    # Aks holda, ingliz tiliga tarjima qilish
    else:
        translation = translator.translate(message.text, dest='en')
        await message.reply(f"Inglizcha: {translation.text}")

    # Tarjima qilingan matnni yuborish
    # await message.reply(f"Tarjima: {translation.text}")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
