from aiogram.types import (ReplyKeyboardMarkup, 
                           KeyboardButton, 
                           InlineKeyboardMarkup, 
                           InlineKeyboardButton
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Автор', callback_data='author')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts'),
     InlineKeyboardButton(text='Запись', callback_data='invoice')]
])

settings = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Написать разработчику', url="tg://user?id=549065222")]
])

name_tg_dict = {'Максим':"tg://user?id=549065222",
                'Шон':"tg://user?id=549065222",
                'Лим':"tg://user?id=549065222"
}
async def inline_name():
    keyboard = InlineKeyboardBuilder()
    for i in name_tg_dict:
        keyboard.add(InlineKeyboardButton(text=i, url=name_tg_dict[i]))
    return keyboard.adjust(2).as_markup()