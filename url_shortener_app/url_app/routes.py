from typing import List

from fastapi import APIRouter, Depends
from starlette import status
from starlette.responses import RedirectResponse

from ..auth.services import fastapi_users
from ..auth.models import UserTable
from . import schemas, utils

# Создание роута для редиректа на указанные url
main_router = APIRouter()


@main_router.get('/{short_path}/')
async def get_link(short_path: str):
    """Функция перенаправления на указанный url."""
    link = await utils.get_link(short_path)

    return RedirectResponse(link, status_code=status.HTTP_302_FOUND)

# Создание роутера для crud
api_router = APIRouter()


@api_router.post('/shortify/', response_model=schemas.URL, status_code=status.HTTP_201_CREATED)
async def create_short_url(url: schemas.URLCreate, user: UserTable = Depends(fastapi_users.current_user())):
    """Функция для создания нового короткого url."""
    return await utils.create_short_url(url=url, user=user)


@api_router.get('/my-shorties/', response_model=List[schemas.URLInfo])
async def get_my_short_url(skip: int = 0, limit: int = 10, user: UserTable = Depends(fastapi_users.current_user())):
    """Функция для получения списка своих url."""
    return await utils.get_my_short_urls(skip, limit, user=user)


@api_router.patch('/my-shorties/{url_id}/', response_model=schemas.URL)
async def get_my_short_url(url_id: int, update_data: schemas.URLUpdate,
                           user: UserTable = Depends(fastapi_users.current_user())):
    """Функция для изменения экземпляра своих url."""
    return await utils.update_my_short_url(url_id, update_data, user=user)


@api_router.delete('/my-shorties/{url_id}/', status_code=status.HTTP_204_NO_CONTENT)
async def get_my_short_url(url_id: int, user: UserTable = Depends(fastapi_users.current_user())):
    """Функция для удаления экземпляра своих url."""
    return await utils.delete_my_short_url(url_id, user=user)
