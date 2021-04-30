import datetime
from typing import Optional

from fastapi_users import models
from pydantic import validator

from ..core.db.database import database
from .models import users


class User(models.BaseUser):
    username: Optional[str] = None
    registration_date: Optional[datetime.date] = None


class UserCreate(models.BaseUserCreate):
    username: str

    @validator('username')
    def valid_username(cls, v: str):
        if len(v) < 2:
            raise ValueError('Username should be at least 2 characters')
        is_username_exists = database.fetch_one(query=users.select())
        if is_username_exists:
            raise ValueError('This username already exists')
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
