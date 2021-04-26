"""
Файл подключения ORM к БД
"""
import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# URL БД
SQLALCHEMY_DATABASE_URL = f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}" \
                          f"@localhost/short_url_db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Класс для создания сессий БД
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Базовый класс для моделей
Base = declarative_base()

