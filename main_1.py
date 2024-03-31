from aiogram import Bot, Dispatcher
from app.database import db_start
from app.handlers import router
from app.middlewares import CheckTime
import asyncio
import logging


TOKEN_API = '7034583895:AAGRl8Ttyp0Nf9QMWS_cI5x5DcE6fl6WGmE'
bot = Bot(token=TOKEN_API)
dp = Dispatcher()

async def on_startup(_):
    await db_start()
    print('Бот запущен')



async def main():
    dp.update.outer_middleware(CheckTime())
    dp.include_router(router)
    await dp.start_polling(bot, on_startup=on_startup)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
