from fastapi_users import FastAPIUsers
from fastapi_users.authentication import JWTAuthentication

from fastapi_users.db import SQLAlchemyUserDatabase

from ..core.config import SECRET_KEY, ACCESS_TOKEN_EXPIRE_SECONDS
from .models import users
from ..core.db.database import database
from .schemas import User, UserCreate, UserUpdate, UserDB

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

