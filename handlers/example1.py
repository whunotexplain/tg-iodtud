from aiogram import F, Router
 
router = Router()

@router.message(F.text == "Aiogrm")
async def aiogram_handler(message):
    await message.answer("... Loves Forever")


@router.callback_query()
async def func(call):
 await call.message.answer('Спасибо, что нажали')
 await call.answer("✅ Выполнено", show_alert=True)
