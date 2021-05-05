from typing import List

from databases import Database
from fastapi import APIRouter, Depends, HTTPException
from starlette import status

from ..auth.services import fastapi_users
from ..auth.models import UserTable
from ..core.db.database import database
from . import schemas, utils

router = APIRouter()


@router.post('/shortify/', response_model=schemas.URL, status_code=status.HTTP_201_CREATED)
async def create_short_url(url: schemas.URLCreate, user: UserTable = Depends(fastapi_users.get_current_user)):
    return await utils.create_short_url(url=url, user=user)


@router.get('/my-shorties/', response_model=List[schemas.URLInfo])
async def get_my_short_url(skip: int = 0, limit: int = 10, user: UserTable = Depends(fastapi_users.get_current_user)):
    return await utils.get_my_short_urls(skip, limit, user=user)


@router.patch('/my-shorties/{url_id}/', response_model=schemas.URL)
async def get_my_short_url(url_id: int, update_data: schemas.URLUpdate,
                           user: UserTable = Depends(fastapi_users.get_current_user)):
    return await utils.update_my_short_url(url_id, update_data, user=user)


@router.delete('/my-shorties/{url_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def get_my_short_url(url_id: int, user: UserTable = Depends(fastapi_users.get_current_user)):
    return await utils.delete_my_short_url(url_id, user=user)


