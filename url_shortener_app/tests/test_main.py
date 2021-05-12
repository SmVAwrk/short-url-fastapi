import asyncio
import datetime

import pytest
from httpx import AsyncClient
from starlette import status

from ..main import app
from ..auth.schemas import UserCreate
from ..auth.services import fastapi_users
from ..core.db.database import database, Base, engine
from ..url_app.models import url_table


@pytest.fixture(autouse=True, scope='function')
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


@pytest.mark.asyncio
async def test_get_link_ok():
    regular_user = await fastapi_users.create_user(
        UserCreate(
            email='test@email.fa',
            username='testname',
            password='test123',
        )
    )

    query = url_table.insert().values(
        title='Test title 1',
        link='http://test.com/test-link/',
        short_url='testshort',
        user_id=regular_user.id,
        created_at=datetime.date.today(),
        link_count=0
    ).returning(url_table)
    url = await database.fetch_one(query)

    async with AsyncClient(app=app, base_url='http://localhost') as client:
        response = await client.get(f'/{url.get("short_url")}/')

    assert response.history[0].status_code == status.HTTP_302_FOUND
    assert response.url == url.get('link')

    query = url_table.select().where(url_table.c.id == url.get('id'))
    updated_url = await database.fetch_one(query)
    assert updated_url.get('link_count') == 1

