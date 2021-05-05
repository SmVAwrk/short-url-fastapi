from fastapi import APIRouter

from .logic import on_after_register, after_verification_request
from .services import jwt_authentication, fastapi_users, SECRET_KEY

# Создание роутера
router = APIRouter()

# Роут для работы с JWT
router.include_router(
    fastapi_users.get_auth_router(jwt_authentication, requires_verification=True),
    prefix="/auth/jwt",
    tags=["auth"],
)

# Роут для регистрации пользователя
router.include_router(
    fastapi_users.get_register_router(after_register=on_after_register),
    prefix="/auth",
    tags=["auth"],
)


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
    fastapi_users.get_verify_router(SECRET_KEY, after_verification_request=after_verification_request),
    prefix="/auth",
    tags=["auth"],
)
