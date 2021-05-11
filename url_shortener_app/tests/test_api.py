import asyncio
import datetime

import pytest
from httpx import AsyncClient
from starlette import status
from starlette.responses import Response

from ..url_app.schemas import URLInfo
from ..auth.services import fastapi_users, jwt_authentication
from ..main import app
from ..core.db.database import Base, engine, database
from ..auth.schemas import UserCreate
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


# @pytest.mark.asyncio
# async def test_url_base_schema():
#     regular_user = await fastapi_users.create_user(
#         UserCreate(
#             email='king.arthur@camelot.bt',
#             username='bull',
#             password='guinevere',
#         )
#     )
#     query = url_table.insert().values(title='Testing1', link='www.leningradspb.ru', short_url='asdsd',
#                                       user_id=regular_user.id, created_at=datetime.date.today(),
#                                       link_count=0).returning(
#         url_table)
#     new_url = await database.fetch_one(query)
#     assert dict(new_url)


@pytest.mark.asyncio
async def test_create_short_url_ok():
    regular_user = await fastapi_users.create_user(
        UserCreate(
            email='test@email.fa',
            username='testname',
            password='test123',
        )
    )
    _ = Response
    jwt_dict = await jwt_authentication.get_login_response(regular_user, _)
    headers = {'Authorization': f'{jwt_dict["token_type"].capitalize()} {jwt_dict["access_token"]}'}

    input_data = {
        'title': 'Test title',
        'link': 'http://test-link.fa',
        'description': 'Test description'
    }

    async with AsyncClient(app=app, base_url='http://test', headers=headers) as client:
        response = await client.post('/api/v1/shortify/', json=input_data)
    assert response.status_code == status.HTTP_201_CREATED

    response_dict = response.json()
    assert response_dict['link'] == 'http://test-link.fa'
    assert response_dict['title'] == 'Test title'
    assert response_dict['description'] == 'Test description'
    assert response_dict['user_id'] == str(regular_user.id)
    assert response_dict.get('id')
    assert response_dict.get('short_url')


@pytest.mark.asyncio
async def test_create_short_url_not_auth():
    input_data = {
        'title': 'Test title',
        'link': 'http://test-link.fa',
        'description': 'Test description'
    }

    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.post('/api/v1/shortify/', json=input_data)
    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.asyncio
async def test_get_my_short_url_ok():
    regular_user = await fastapi_users.create_user(
        UserCreate(
            email='test@email.fa',
            username='testname',
            password='test123',
        )
    )
    _ = Response
    jwt_dict = await jwt_authentication.get_login_response(regular_user, _)
    headers = {'Authorization': f'{jwt_dict["token_type"].capitalize()} {jwt_dict["access_token"]}'}

    query = url_table.insert().values(
        title='Test title 1',
        link='http://test-link.fa',
        short_url='testshort',
        user_id=regular_user.id,
        created_at=datetime.date.today(),
        link_count=0
    ).returning(url_table)
    url = await database.fetch_one(query)
    url_dict = dict(url)

    async with AsyncClient(app=app, base_url='http://test', headers=headers) as client:
        response = await client.get('/api/v1/my-shorties/')
    assert response.status_code == status.HTTP_200_OK

    serialized_url = URLInfo(**url_dict).dict()
    serialized_url['created_at'] = serialized_url['created_at'].strftime('%Y-%m-%d')
    serialized_url['link'] = str(serialized_url['link'])
    expected_data = [
        serialized_url
    ]

    assert response.json() == expected_data


@pytest.mark.asyncio
async def test_get_my_short_url_not_auth():
    async with AsyncClient(app=app, base_url='http://test') as client:
        response = await client.get('/api/v1/my-shorties/')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED
