from typing import List
from aiogram.filters import BaseFilter
from aiogram.types import Message

class IsAdmin(BaseFilter):

    def __init__(self, users_id: int | List[int]) -> None:
        self.users_id = users_id

    async def __call__(self, message: Message) -> bool:
       
       if isinstance(self.users_id, int):
        return message.from_user.id == self.users_id
       return message.from_user.id in self.user_id
        
    