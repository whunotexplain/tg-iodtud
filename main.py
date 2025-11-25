from aiogram import F, Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
import asyncio
import config
import logging
import keyboard
from keyboard import example
from handlers import example1, example2

api = config.api_key
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())
logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    filemode="a",
    format="% (asctime)s %(levelname)s %(message)s"
    )

@dp.message()
async def hello_handler(message):
    print("Something")

@dp.callback_query()
async def func(call):
    print("smth was callable")

@dp.message(F.text == "Information")
async def get_information(message):
    await message.answer("Всю необходимую информацию можете найти на нашем сайте",
        reply_markup=keyboard.example.main_kb)
    
@dp.message()
async def start(message):
 # Отвечаем на сообщение
    await message.answer("Приветик!", reply_markup=keyboard.example.menu)

async def main():
    dp.include_routers(example1.router, example2.router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())