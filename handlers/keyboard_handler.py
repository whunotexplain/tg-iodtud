import keyboard
from aiogram import Dispatcher

from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import F


dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.text == "Information")
async def get_info(message):
    await message.answer

