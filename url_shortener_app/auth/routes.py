from fastapi import APIRouter
from starlette.requests import Request

from ..core.config import EMAIL_AVAILABLE
from ..core.utils import send_email
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


def on_after_register(user: UserDB, request: Request):
    print(f"User {user.username} has registered.")


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


def after_verification_request(user: UserDB, token: str, request: Request):
    if EMAIL_AVAILABLE:
        message = f"""
        Subject: Верификация токена
        
        
        Verification requested for user {user.username}. 
        Verification token: {token}
        """.encode(encoding='utf8')
        send_email(user.email, message)
    print(f"Verification requested for user {user.id}. Verification token: {token}")


# Роут для верификации
router.include_router(
    fastapi_users.get_verify_router(SECRET_KEY, after_verification_request=after_verification_request),
    prefix="/auth",
    tags=["auth"],
)
