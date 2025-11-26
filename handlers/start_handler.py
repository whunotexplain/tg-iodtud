from aiogram.filters import CommandStart
from aiogram import Router


router = Router()


@router.message(CommandStart())
async def start(message):
    await message.answer("Apprecate to see u ")