from aiogram import F, Router
 

router = Router()

@router.message()
async def start_handler(message):
    await message.answer("hello")

