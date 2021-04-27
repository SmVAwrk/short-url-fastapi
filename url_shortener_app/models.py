from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from passlib.apps import custom_app_context as password_hasher

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=128), unique=True, nullable=False, index=True )
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    # lazy - не ставить 'dynamic', т.к. ругается pydantic
    urls = relationship(
        'URL',
        back_populates='owner',
        passive_deletes=True,
        cascade='all, delete'
    )

    def __repr__(self):
        return f'<User: {self.username}>'

    def hash_password(self, password: str):
        """Метод хеширования пароля."""
        self.password_hash = password_hasher.hash(password)

    def verify_password(self, password: str):
        """Метод проверки пароля."""
        return password_hasher.verify(password, self.password_hash)


class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String, index=True, nullable=False)
    short_url = Column(String, index=True, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
    title = Column(String(length=128), nullable=False)
    description = Column(String(length=512))

    owner = relationship(
        User,
        back_populates='urls'
    )

    def __repr__(self):
        return f'<URL: {self.short_url}>'
