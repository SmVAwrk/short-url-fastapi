import datetime
from typing import Optional

from fastapi_users import models
from pydantic import validator


class User(models.BaseUser):
    username: Optional[str] = None
    registration_date: Optional[datetime.date] = None


class UserCreate(models.BaseUserCreate):
    username: str

    @validator('username')
    def valid_username(cls, v: str):
        if len(v) < 2:
            raise ValueError('Username should be at least 2 characters')
        return v

    @validator('password')
    def valid_password(cls, v: str):
        if len(v) < 6:
            raise ValueError('Password should be at least 6 characters')
        return v


class UserUpdate(User, models.BaseUserUpdate):
    pass


class UserDB(User, models.BaseUserDB):
    username: str
    registration_date: Optional[datetime.date] = datetime.date.today()
