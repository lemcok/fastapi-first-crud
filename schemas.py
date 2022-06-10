from asyncio import Task
from pydantic import BaseModel

class Item(BaseModel):
   task: str
   # rating: int