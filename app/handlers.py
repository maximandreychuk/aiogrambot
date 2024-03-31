from aiogram import F, Router
from aiogram.types import (ReplyKeyboardMarkup, 
                           KeyboardButton)
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
import app.keyboards as kb
from app.filters import IsAdmin

# router = Router()
from app.bot import router
class Reg(StatesGroup):
    name = State()
    numb = State()

@router.message(Command('reg'))
async def reg_one(message: Message, state: FSMContext):
    await state.set_state(Reg.name)
    await message.answer("Введите ваше имя")

@router.message(Reg.name)
async def reg_two(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Reg.numb)
    await message.answer("Введите время")

@router.message(Reg.numb)
async def reg_three(message: Message, state: FSMContext):
    await state.update_data(numb=message.text)
    await state.set_state(Reg.numb)
    data = await state.get_data()
    await message.answer(f"Регистрация завершена, твое имя - {data["name"]}, время - {data["numb"]}")
    await state.clear


@router.message(F.text == "Как дела?") #сравниваем с сообщением пользователя
async def how_are_you(message: Message):
    await message.answer(text="Ok")

@router.message(F.photo)  
async def get_photo_id(message: Message):
    await message.answer(f'id photo: {message.photo[-1].file_id}')

@router.message(Command('get_photo'))  
async def get_photo(message: Message):
    await message.answer_photo(photo='AgACAgIAAxkBAAMgZf2LX-6S1XGA-7GjgKOcnJ0-zLMAAk7cMRtd_PFLlEIWTDvQY4MBAAMCAANtAAM0BA',
                               caption = 'wm')

@router.message(Command('info'))  
async def get_info(message: Message):
    await message.answer(text="Это команда /info")

@router.message(Command('help'))  
async def get_help(message: Message):
    await message.answer(text="Это команда /help")

# @router.message(CommandStart)
# async def cmd_start(message: Message):
#     await message.reply(text=f'Привет, {message.from_user.first_name}, твой id - {message.from_user.id}',
#                         reply_markup = kb.main)

@router.callback_query(F.data=='author')
async def author(callback: CallbackQuery):
    await callback.answer('Вы выбрали Автор', show_alert=True)
    await callback.message.edit_text('Выбирай', reply_markup=await kb.inline_name())


"""Разработка бота."""
class RegToWork(StatesGroup, State):
    time = State()
    way = State()

@router.message(Command('gol'))
async def sap_step_one(message: Message, state: FSMContext):
    await state.set_state(RegToWork.time)
    await message.answer(text="К какому времени?", reply_markup = await kb.make_time_keyboard())

@router.message(RegToWork.time)
async def sap_step_two(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await state.set_state(RegToWork.way)
    await message.answer(text="Выбери", reply_markup= await kb.make_way_keyboard())

@router.message(RegToWork.way)
async def sap_step_three(message: Message, state: FSMContext):
    await state.update_data(way=message.text)
    data = await state.get_data()
    await message.answer(f"Поздравляю, ты записан на {data["time"]}, {data["way"]}", reply_markup=kb.rmk)
    await state.clear
