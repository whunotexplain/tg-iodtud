from aiogram.filters import Command
from aiogram import Router

router = Router()


@router.message(Command("/help"))
async def help(message):
    await message.answer(f"Admin can help")

@router.message(Command('help', prefix='!'))
async def help(message):
    await message.answer('За помощью обратитесь к администратору @koz2based')
