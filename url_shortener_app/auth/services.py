from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from fastapi_users.db import SQLAlchemyUserDatabase

from ..core.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_SECONDS
from .models import users_table
from ..core.db.database import database
from .schemas import User, UserCreate, UserUpdate, UserDB

# Создание адаптера для связи между БД и логикой users
user_db = SQLAlchemyUserDatabase(UserDB, database, users_table)

auth_backends = []

# Создание JWT auth
jwt_authentication = JWTAuthentication(secret=SECRET_KEY, lifetime_seconds=ACCESS_TOKEN_EXPIRE_SECONDS)

auth_backends.append(jwt_authentication)

# Подключение всех элементов
fastapi_users = FastAPIUsers(
    user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)

