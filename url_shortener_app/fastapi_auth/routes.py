from fastapi import APIRouter
from starlette.requests import Request

from .schemas import UserDB
from .services import jwt_authentication, fastapi_users, SECRET_KEY

# Создаем роутер
router = APIRouter()

# Роут для работы с JWT
router.include_router(
    fastapi_users.get_auth_router(jwt_authentication),
    prefix="/auth/jwt",
    tags=["auth"],
)

# Роут для регистрации пользователя
router.include_router(
    fastapi_users.get_register_router(),
    prefix="/auth",
    tags=["auth"],
)


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.id} has registered.")


# Роут для сброса пароля
router.include_router(
    fastapi_users.get_reset_password_router(SECRET_KEY),
    prefix="/auth",
    tags=["auth"],
)

# Роут для получения списка пользователей
router.include_router(
    fastapi_users.get_users_router(),
    prefix="/users",
    tags=["users"],
)

# Роут для верификации
router.include_router(
    fastapi_users.get_verify_router(SECRET_KEY),
    prefix="/auth",
    tags=["auth"],
)
