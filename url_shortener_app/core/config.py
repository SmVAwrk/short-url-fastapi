import os

# Корневая директория
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Секретный ключ
SECRET_KEY = '26ebaf0dfd26a223e987fa5b2d0f8667d9bbb050d872a7a316b08fe8ecfa01a3'

# Режим дебаг
DEBUG = False

# Режим для тестов
TEST_MODE = False

# Длительность действия auth токена
ACCESS_TOKEN_EXPIRE_SECONDS = 60 * 60 * 24 * 7

# Настройки БД
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
POSTGRES_HOST = os.environ.get('POSTGRES_HOST', 'localhost')
POSTGRES_DB = os.environ.get('POSTGRES_DB', 'short_url_db')
POSTGRES_TEST_DB = os.environ.get('POSTGRES_DB', 'test_short_url_db')


# URL базы данных
SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_DB}"
# URL тестовой базы данных
SQLALCHEMY_TEST_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}/{POSTGRES_TEST_DB}"

# Настройки отправки email
EMAIL_PORT = 587
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_AVAILABLE = bool(EMAIL_HOST and EMAIL_HOST_PASSWORD and EMAIL_HOST)
