from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from fastapi_users.db import SQLAlchemyUserDatabase

from .models import UserTable
from ..db.database import SessionLocal, database
from .schemas import User, UserCreate, UserUpdate, UserDB

# Секретный ключ для JWT
SECRET_KEY = '26ebaf0dfd26a223e987fa5b2d0f8667d9bbb050d872a7a316b08fe8ecfa01a3'

# Длительность действия токена
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 60 * 24

users = UserTable.__table__
user_db = SQLAlchemyUserDatabase(UserDB, database, users)

auth_backends = []

jwt_authentication = JWTAuthentication(secret=SECRET_KEY, lifetime_seconds=ACCESS_TOKEN_EXPIRE_SECONDS)

auth_backends.append(jwt_authentication)


fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)