from fastapi import HTTPException
from sqlalchemy import desc
from starlette import status

from .permissions import check_owner_or_admin
from ..core.utils import get_unique_path, get_object_or_404
from .models import url_table
from ..auth.models import UserTable
from ..core.db.database import database
from . import schemas


async def get_link(short_path: str):
    """Функция для получения полного url."""
    url = await get_object_or_404(url_table, short_url=short_path)

    update_query = url_table.update().values(link_count=url_table.c.link_count + 1).where(
        url_table.c.short_url == short_path)

    await database.execute(update_query)

    return url.get('link')


async def create_short_url(url: schemas.URLCreate, user: UserTable):
    query = url_table.insert().values(**url.dict(), user_id=user.id, short_url=get_unique_path()).returning(url_table)
    new_url = await database.fetch_one(query)

    return dict(new_url)


async def get_my_short_urls(skip: int, limit: int, user: UserTable):
    query = url_table.select().where(url_table.c.user_id == user.id).order_by(desc(url_table.c.created_at)).offset(
        skip).limit(limit)
    my_urls = await database.fetch_all(query)

    return [dict(url) for url in my_urls]


async def update_my_short_url(url_id: int, update_data: schemas.URLUpdate, user: UserTable):
    url = await get_object_or_404(url_table, id=url_id)

    if not update_data.dict(exclude_unset=True):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='Empty data')

    check_owner_or_admin(url, user)

    update_query = url_table.update().values(**update_data.dict(exclude_unset=True)).where(
        url_table.c.id == url_id).returning(url_table)
    updated_url = await database.fetch_one(update_query)

    return dict(updated_url)


async def delete_my_short_url(url_id: int, user: UserTable):
    url = await get_object_or_404(url_table, id=url_id)

    check_owner_or_admin(url, user)

    delete_query = url_table.delete().where(url_table.c.id == url_id)
    await database.execute(delete_query)

    return
