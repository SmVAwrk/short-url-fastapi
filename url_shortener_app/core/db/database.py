"""
Файл подключения ORM к БД
"""

import databases
from sqlalchemy import create_engine

from ..config import SQLALCHEMY_DATABASE_URL
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(SQLALCHEMY_DATABASE_URL)
# # Класс для создания сессий БД
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Создание экземпляра database для работы с БД
database = databases.Database(SQLALCHEMY_DATABASE_URL)

# Базовый класс для моделей
Base = declarative_base()

