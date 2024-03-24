from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
import app.keyboards as kb


router = Router()
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

@router.message(CommandStart)
async def cmd_start(message: Message):
    await message.reply(text=f'Привет, {message.from_user.first_name}, твой id - {message.from_user.id}',
                        reply_markup = kb.main)

@router.callback_query(F.data=='author')
async def author(callback: CallbackQuery):
    await callback.answer('Вы выбрали Автор', show_alert=True)
    await callback.message.edit_text('Выбирай', reply_markup=await kb.inline_name())
