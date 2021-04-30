"""
Схемы, связанные с аутентификацией и регистрацией.
"""

import datetime
from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    """Схема для возврата созданного токена пользователю."""
    access_token: str
    token_type: str


class TokenData(BaseModel):
    """Схема для передачи имени пользователя."""
    username: Optional[str]


class User(BaseModel):
    """Схема для представления пользователя."""
    username: str
    email: str

    class Config:
        orm_mode = True


class UserCreate(User):
    """Схема для создания пользователя."""
    password: str


class InspectUser(User):
    """Схема для представления информации о пользователе."""
    is_active: bool
    is_admin: bool
    registration_date: datetime.date


