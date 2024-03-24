from aiogram import Bot, Dispatcher
from app.handlers import router
import asyncio
import logging


TOKEN_API = '7034583895:AAGRl8Ttyp0Nf9QMWS_cI5x5DcE6fl6WGmE'
bot = Bot(token=TOKEN_API)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
