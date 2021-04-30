import os

# Корневая директория
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Секретный ключ
SECRET_KEY = '26ebaf0dfd26a223e987fa5b2d0f8667d9bbb050d872a7a316b08fe8ecfa01a3'

# Длительность действия auth токена
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 60 * 24

# URL базы данных
SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}" \
                          f"@localhost/short_url_db"

# Настройки отправки email
EMAIL_PORT = 587
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_AVAILABLE = bool(EMAIL_HOST and EMAIL_HOST_PASSWORD and EMAIL_HOST)
