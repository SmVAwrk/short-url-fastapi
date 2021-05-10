import asyncio
import datetime

import pytest
from httpx import AsyncClient
from starlette.testclient import TestClient

from ..main import app
from ..core.db.database import Base
from ..auth.schemas import UserCreate
from .db_test_settings import test_fastapi_users, test_database, test_engine
from ..url_app.models import url_table


@pytest.fixture(autouse=True, scope='module')
async def init_db():
    Base.metadata.create_all(bind=test_engine)
    await test_database.connect()

    yield

    await test_database.disconnect()
    Base.metadata.drop_all(bind=test_engine)


@pytest.fixture(scope='module')
def event_loop():
    loop = asyncio.get_event_loop()
    yield loop
    loop.close()




@pytest.mark.asyncio
async def test_url_base_schema():
    regular_user = await test_fastapi_users.create_user(
        UserCreate(
            email='king.arthur@camelot.bt',
            username='bull',
            password='guinevere',
        )
    )
    query = url_table.insert().values(title='Testing1', link='www.leningradspb.ru', short_url='asdsd',
                                      user_id=regular_user.id, created_at=datetime.date.today(),
                                      link_count=0).returning(
        url_table)
    new_url = await test_database.fetch_one(query)
    assert dict(new_url)


@pytest.mark.asyncio
async def test_root():
    async with AsyncClient(app=app, base_url="http://test") as client:
        response = await client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Tomato"}