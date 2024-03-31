from aiogram.types import (ReplyKeyboardMarkup, 
                           KeyboardButton, 
                           InlineKeyboardMarkup, 
                           InlineKeyboardButton,
                           ReplyKeyboardRemove,
)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder


way = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Авто', callback_data='auto')],
    [InlineKeyboardButton(text='Пешком', callback_data='fuss')],
])
time = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='12')],
    [KeyboardButton(text='14')],
    [KeyboardButton(text='16')]
])
main = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Автор', callback_data='author')],
    [InlineKeyboardButton(text='Контакты', callback_data='contacts'),
     InlineKeyboardButton(text='Запись', callback_data='invoice')]
])

settings = InlineKeyboardMarkup(
    inline_keyboard=[[InlineKeyboardButton(text='Написать разработчику', url="tg://user?id=549065222")]
])

# name_tg_dict = {'Максим':"tg://user?id=549065222",
#                 'Шон':"tg://user?id=549065222",
#                 'Лим':"tg://user?id=549065222"
# }
# async def inline_name():
#     keyboard = InlineKeyboardBuilder()
#     for i in name_tg_dict:
#         keyboard.add(InlineKeyboardButton(text=i, url=name_tg_dict[i]))
#     return keyboard.adjust(2).as_markup()

async def make_time_keyboard(lst=['12','14','16']):
    return ReplyKeyboardMarkup(keyboard=[KeyboardButton(text='Тык')], resize_keyboard=True)

"""Разработка бота."""

rmk = ReplyKeyboardRemove() #для удаления реплай клавы

go_to_reg = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Погнали')]],resize_keyboard=True)
is_good = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Хорошо')]],resize_keyboard=True)

async def make_time_keyboard(lst=['12','14','16']):
    kb=[KeyboardButton(text=item) for item in lst]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)

async def make_way_keyboard(lst=['На машине', 'Пешком']):
    kb=[KeyboardButton(text=item) for item in lst]
    return ReplyKeyboardMarkup(keyboard=[kb], resize_keyboard=True)