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
