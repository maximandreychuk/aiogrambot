from aiogram import Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from app import keyboards as kb
import asyncpg

router = Router()

class RegToWork(StatesGroup, State):
    ready = State()
    time = State()
    way = State()

@router.message(Command('start'))
async def check_time(message: Message,
                     curr_hour: int,
                     state: FSMContext):
    msg_if_true = f'Сейчас {curr_hour} часов, ты можешь записываться'
    msg_if_false = f'Сейчас {curr_hour} часов, подожди 18 часов'
    if curr_hour >= 10 and curr_hour <= 23:  # время для теста
        await message.answer(msg_if_true, reply_markup = kb.go_to_reg)
        await state.set_state(RegToWork.ready)
    else: await message.answer(msg_if_false, reply_markup = kb.is_good)

@router.message(Command('db'))
async def create_db(message: Message, db: asyncpg.pool.Pool):
    await db.execute("CREATE TABLE IF NOT EXISTS couriers("
                "id INTEGER PRIMARY KEY, "
                "data TEXT"
                "work_time TEXT, "
                "method TEXT)")
    await message.answer('Привет! Таблица couriers создана.')

@router.message(RegToWork.ready)
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
