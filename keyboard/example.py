from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard= [
        KeyboardButton(text="Information")
    ]
)


in_kb = ReplyKeyboardMarkup(
 keyboard=[
    [
        KeyboardButton(text="Администрторы"),
        KeyboardButton(text="Пользователи"),
    ],
    [
        KeyboardButton(text="Статистика"),
        KeyboardButton(text="Платежи"),
        KeyboardButton(text="Активность"),
    ],
    [
        KeyboardButton(text="Заблокировать"),
        KeyboardButton(text="Разблокировать"),
    ],
 ],
)