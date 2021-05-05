import datetime
from typing import Optional

from pydantic import BaseModel, HttpUrl, UUID4


class URLBase(BaseModel):
    link: HttpUrl
    title: str


class URLCreate(URLBase):
    description: Optional[str] = None


class URLUpdate(BaseModel):
    link: Optional[HttpUrl]
    title: Optional[str]
    description: Optional[str]


class URL(URLBase):
    id: int
    user_id: UUID4
    short_url: str
    description: Optional[str] = None

    # class Config:
    #     # Говорит pydantic работать не только с диктами, а с любыми типами
    #     orm_mode = True


class URLInfo(URLBase):
    id: int
    short_url: str
    description: Optional[str] = None
    link_count: int = 0
    created_at: datetime.date = datetime.date.today()

    # class Config:
    #     orm_mode = True
