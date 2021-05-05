from starlette.requests import Request

from ..core.utils import send_email
from ..core.config import EMAIL_AVAILABLE
from .schemas import UserDB


def on_after_register(user: UserDB, request: Request):
    """Функция для исполнения логики после регистрации."""
    print(f"User {user.username} has registered.")


def after_verification_request(user: UserDB, token: str, request: Request):
    """
    Функция для исполнения логики после запроса на верификацию.
    (Отправка сообщения с токеном подтверждения на почту)
    """
    if EMAIL_AVAILABLE:
        message = f"""
        Subject: Верификация токена


        Verification requested for user {user.username}. 
        Verification token: {token}
        """.encode(encoding='utf8')
        send_email(user.email, message)
    print(f"Verification requested for user {user.id}. Verification token: {token}")