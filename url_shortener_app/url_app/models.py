from datetime import date

from fastapi_users.db.sqlalchemy import GUID
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from ..core.db.database import Base


class URL(Base):
    """Модель сокращаемых URL."""
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String, index=True, nullable=False)
    short_url = Column(String, index=True, nullable=False)
    user_id = Column(GUID, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(length=128), nullable=False)
    created_at = Column(Date, default=date.today())
    description = Column(String(length=512))
    link_count = Column(Integer, default=0)

    owner = relationship('UserTable', back_populates='urls')

    def __repr__(self):
        return f'<URL: {self.short_url}>'


# Получение объекта таблицы url для работы с database
url_table = URL.__table__
