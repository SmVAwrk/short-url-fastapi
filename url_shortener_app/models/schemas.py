# from typing import List, Optional
#
# from pydantic import BaseModel
#
#
# class URLBase(BaseModel):
#     link: str
#     title: str
#
#
# class URLCreate(URLBase):
#     description: Optional[str]
#
#
# class URL(URLBase):
#     id: int
#     user_id: int
#     short_url: str
#     description: Optional[str] = None
#
#     class Config:
#         # Говорит pydantic работать не только с диктами, а с любыми типами
#         orm_mode = True
#
#
