import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl, UUID4


class URLBase(BaseModel):
    """Базовая схема для URL."""
    link: HttpUrl
    title: str


class URLCreate(URLBase):
    """Схема для создания URL."""
    description: Optional[str] = None
    link_count: int = 0
    created_at: datetime.date = datetime.date.today()


class URLUpdate(BaseModel):
    """Схема для изменения URL."""
    link: Optional[HttpUrl]
    title: Optional[str]
    description: Optional[str]


class URL(URLBase):
    """Схема для представления URL."""
    id: int
    user_id: UUID4
    short_url: str
    description: Optional[str] = None


class URLInfo(URLBase):
    """Схема для получения информации о своем URL"""
    id: int
    short_url: str
    description: Optional[str] = None
    link_count: int
    created_at: datetime.date

