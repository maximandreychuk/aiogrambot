from aiogram import Bot, Dispatcher
from app import database as db
from app.handlers import router
from app.middlewares import CheckTime, DatabaseMiddleware
import asyncio
import logging
from aiogram.fsm.storage.memory import MemoryStorage



TOKEN_API = '7034583895:AAGRl8Ttyp0Nf9QMWS_cI5x5DcE6fl6WGmE'
bot = Bot(token=TOKEN_API)
dp = Dispatcher()

# async def on_startup(_):
#     await db.db_start()
#     print('Бот успешно запущен')


async def main():
    dp.update.outer_middleware(CheckTime())
    dp.middleware.setup(DatabaseMiddleware())
    dp.include_router(router)
    await dp.start_polling(bot, storage=MemoryStorage())

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
