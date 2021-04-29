from typing import List, Optional

from pydantic import BaseModel


class URLBase(BaseModel):
    link: str
    title: str


class URLCreate(URLBase):
    description: Optional[str]


class URL(URLBase):
    id: int
    user_id: int
    short_url: str
    description: Optional[str] = None

    class Config:
        # Говорит pydantic работать не только с диктами, а с любыми типами
        orm_mode = True


class UserBase(BaseModel):
    username: str


# class UserList(UserBase):
#     pass


class UserCreate(UserBase):
    email: str
    password: str


class User(UserBase):
    id: int
    email: str
    urls: List[URL] = []

    class Config:
        orm_mode = True
