import logging
import secrets
import smtplib
import ssl
import string

from fastapi import HTTPException
from sqlalchemy import and_
from starlette import status

from .config import EMAIL_PORT, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD
from .db.database import database

PATH_LENGTH = 8

logger = logging.getLogger(__name__)


def send_email(
        receiver_email,
        message,
        port=EMAIL_PORT,
        smtp_server=EMAIL_HOST,
        sender_email=EMAIL_HOST_USER,
        password=EMAIL_HOST_PASSWORD
):
    """Функция для отправки email-сообщения пользователю."""
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)
        logger.debug(f'Выполнена отправка сообщения на {receiver_email}.')


def get_unique_path():
    """Функция для генерации случайного короткого пути для ссылки."""
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits

    return ''.join([secrets.choice(chars) for _ in range(PATH_LENGTH)])


async def get_object_or_404(table, **kwargs):
    """
    Функция для получения объекта из БД.
    :param table: Объект таблицы из которой необходимо получить данные
    :param kwargs: Поля и значения, по которым нужно идентифицировать запись
    :return: Объект записи из таблицы или raise 404 ошибки
    """
    expression = [getattr(table.c, key) == value for key, value in kwargs.items()]
    query = table.select().where(and_(*expression))
    object_ = await database.fetch_one(query)
    if not object_:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Object not found')

    return object_
