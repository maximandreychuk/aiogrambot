import asyncpg
from aiogram import BaseMiddleware
from aiogram.types import Message
from datetime import datetime
from typing import Any, Callable, Dict, Awaitable
from aiogram.types import TelegramObject


class CheckTime(BaseMiddleware):
    async def __call__(
                self,
                handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
                event: TelegramObject,
                data: Dict[str, Any],
        ) -> Any:
        curr_hour: int = datetime.today().hour
        data["curr_hour"] = curr_hour
        return await handler(event, data)
    
class DatabaseMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.pool = None

    async def pre_process(self, obj, data, *args):
        if not self.pool:
            self.pool = await asyncpg.create_pool(
                user='USER',
                password='PASSWORD',
                database='DATABASE',
                host='HOST'
            )
        data['db'] = self.pool

    async def post_process(self, obj, data, *args):
        pass

