from datetime import date

from fastapi_users.db import SQLAlchemyBaseUserTable
from sqlalchemy import Column, String, Date
from sqlalchemy.orm import relationship

from ..core.db.database import Base
from ..url_app.models import URL


class UserTable(Base, SQLAlchemyBaseUserTable):
    """Расширение модели пользователя бибилотеки fastapi_users."""
    __tablename__ = 'users'

    username = Column(String(length=64), unique=True, index=True, nullable=False)
    registration_date = Column(Date, default=date.today())

    # Создание отношения к модели URL
    # lazy - не ставить 'dynamic', т.к. ругается pydantic
    urls = relationship(
        URL,
        back_populates='owner',
        passive_deletes=True,
        cascade='all, delete'
    )


# Получение объекта таблицы пользователей для работы с database
users_table = UserTable.__table__
