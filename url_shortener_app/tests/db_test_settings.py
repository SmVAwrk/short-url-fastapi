import databases
import sqlalchemy
from fastapi_users import FastAPIUsers
from fastapi_users.db import SQLAlchemyUserDatabase
from sqlalchemy import create_engine

from ..auth.services import auth_backends
from ..auth.models import users_table
from ..auth.schemas import UserDB, User, UserCreate, UserUpdate
from ..core.config import SQLALCHEMY_TEST_DATABASE_URL

# Тестовый engine
test_engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)

# Тестовая БД
test_database = databases.Database(SQLALCHEMY_TEST_DATABASE_URL, force_rollback=True)

# Метаданные
test_metadata = sqlalchemy.MetaData()

# Создание всех таблиц
test_metadata.create_all(test_engine)

# FastAPI Users
test_user_db = SQLAlchemyUserDatabase(UserDB, test_database, users_table)

test_fastapi_users = FastAPIUsers(
    test_user_db,
    auth_backends,
    User,
    UserCreate,
    UserUpdate,
    UserDB,
)
