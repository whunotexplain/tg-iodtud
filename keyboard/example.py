from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, \
                            InlineKeyboardButton, InlineKeyboardMarkup

from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Каталог", callback_data='catalog')],
    [InlineKeyboardButton(text="Корзина", callback_data='bucket'),
    InlineKeyboardButton(text="контакты", callback_data='contacts')],
])

settings = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Instagram", url="https://instagram.com/whynotkozyyy")]
    ])

cars = ['Tesla', "BMW", "Mercedes"]

async def inline_cars():
    keyboard = InlineKeyboardBuilder()
    for car in cars:
        keyboard.add(InlineKeyboardButton(text=car, url="https://instagram.com/whynotkozyyy"))
    return keyboard.adjust(2).as_markup()