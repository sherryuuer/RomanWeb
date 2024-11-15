from pydantic import BaseModel
from typing import List

class UserBase(BaseModel):
    email: str
    username: str
    first_name: str
    last_name: str
    gender: str
    country: str
    isActive: bool

class User(UserBase):
    id: int
    class Config:
        orm_mode = True

class UserCreate(UserBase):
    password: str