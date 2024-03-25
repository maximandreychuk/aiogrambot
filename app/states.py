from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import .keyboards as kb

router = Router()

class RegToWork(StatesGroup, State):
    time = State()
    way = State()

@router.message(Command('gol'))
async def sap_step_one(message: Message, state: FSMContext):
    await message.answer(text="К какому времени?", reply_markup = await kb.make_time_keyboard())
    await state.set_state(RegToWork.time)

@router.message(RegToWork.time)
async def sap_step_two(message: Message, state: FSMContext):
    await state.update_data(time=message.text)
    await message.answer(text="Выбери", reply_markup= await kb.make_way_keyboard())
    await state.set_state(RegToWork.way)

@router.message(RegToWork.way)
async def sap_step_three(message: Message, state: FSMContext):
    await state.update_data(way=message.text)
    data = await state.get_data()
    await message.answer(f"Поздравляю, твое время - {data["time"]}, {data["way"]}")
    await state.clear
