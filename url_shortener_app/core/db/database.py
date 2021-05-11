"""
Файл подключения ORM к БД
"""

import databases
from sqlalchemy import create_engine

from ..config import SQLALCHEMY_DATABASE_URL, TEST_MODE, SQLALCHEMY_TEST_DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base

# Старт SQLAlchemy engine
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Создание экземпляра database для работы с БД
database = databases.Database(SQLALCHEMY_DATABASE_URL)

# Базовый класс для моделей
Base = declarative_base()

# Подключение тестовой БД при тестах
if TEST_MODE:
    engine = create_engine(SQLALCHEMY_TEST_DATABASE_URL)
    database = databases.Database(SQLALCHEMY_TEST_DATABASE_URL, force_rollback=True)

