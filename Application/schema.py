from pydantic import BaseModel
from typing import List

class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    class Config:
        orm_mode = True