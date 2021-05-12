import asyncio
import datetime

import pytest
from fastapi import HTTPException

from ..auth.schemas import UserCreate
from ..auth.services import fastapi_users
from ..core.db.database import Base, engine, database
from ..url_app.models import url_table
from ..core.utils import get_unique_path, PATH_LENGTH, get_object_or_404

TEST_PATHS_QUANTITY = 10


@pytest.fixture(scope='function')
async def init_db():
    Base.metadata.create_all(bind=engine)
    await database.connect()

    yield

    await database.disconnect()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope='module')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()


def test_get_unique_path():
    unique_paths = []
    for _ in range(TEST_PATHS_QUANTITY):
        unique_str = get_unique_path()
        unique_paths.append(unique_str)

    assert len(unique_paths[0]) == PATH_LENGTH
    assert len(unique_paths) == len(set(unique_paths))


@pytest.mark.asyncio
async def test_get_object_or_404_object_exist(init_db):
    regular_user = await fastapi_users.create_user(
        UserCreate(
            email='test@email.fa',
            username='testname',
            password='test123',
        )
    )
    query = url_table.insert().values(
        title='Test title 1',
        link='http://test-link.fa',
        short_url='testshort',
        user_id=regular_user.id,
        created_at=datetime.date.today(),
        link_count=0
    ).returning(url_table)
    url = await database.fetch_one(query)

    object_ = await get_object_or_404(url_table, id=url.get('id'))

    assert object_ == url


@pytest.mark.asyncio
async def test_get_object_or_404_object_not_exist(init_db):
    regular_user = await fastapi_users.create_user(
        UserCreate(
            email='test@email.fa',
            username='testname',
            password='test123',
        )
    )
    query = url_table.insert().values(
        title='Test title 1',
        link='http://test-link.fa',
        short_url='testshort',
        user_id=regular_user.id,
        created_at=datetime.date.today(),
        link_count=0
    )
    await database.execute(query)

    with pytest.raises(HTTPException):
        await get_object_or_404(url_table, id=-1)
