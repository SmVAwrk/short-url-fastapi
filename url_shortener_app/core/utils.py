import secrets
import smtplib
import ssl
import string

from .config import EMAIL_PORT, EMAIL_HOST, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD

PATH_LENGTH = 8


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


def get_unique_path():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    return ''.join([secrets.choice(chars) for _ in range(PATH_LENGTH)])
