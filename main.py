from aiogram import F, Bot, Dispatcher, Router
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart, Command
import asyncio
import config
import logging
# from handlers import start_handler, help_handler
import keyboard.example as kb
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from middleware import TestMiddleware

class Registartion(StatesGroup):
    name = State()
    number = State()


api = config.api_key
bot = Bot(token=api)
dp = Dispatcher(storage=MemoryStorage())


router = Router()
router.message.middleware(TestMiddleware())



logging.basicConfig(
    level=logging.INFO,
    filename="logs.log",
    filemode="a",
    format="% (asctime)s %(levelname)s %(message)s"
    )

@dp.message(CommandStart())
async def start_cmd(message: Message):
    await message.reply(f"Hello, you!\n Ur id = {message.from_user.id}\n Ur name = {message.from_user.first_name}", 
                        reply_markup=kb.main)
    

@dp.callback_query(F.data == 'catalog')
async def catalog(callback: CallbackQuery):
    await callback.answer('')
    await callback.message.edit_text('Привет', reply_markup=await kb.inline_cars())

@dp.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Registartion.name)
    await message.answer("Введите ваше имя")


@dp.message(Registartion.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Registartion.number)
    await message.answer("Введите номер телефона")


@dp.message(Registartion.number)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(number=message.text)
    data = await state.get_data()
    await message.answer(f"Спасибо за регистрацию\n Name: {data['name']}\nPhone number: {data['number']}")
    await state.clear()




async def main():
    # dp.include_routers()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())