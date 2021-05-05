from datetime import date

from fastapi_users.db.sqlalchemy import GUID
from sqlalchemy import Column, Integer, String, ForeignKey, event, Date
from sqlalchemy.orm import relationship

from ..core.db.database import Base, database


# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(length=128), unique=True, nullable=False, index=True )
#     email = Column(String, unique=True, nullable=False, index=True)
#     password_hash = Column(String, nullable=False)
#     is_active = Column(Boolean, default=False)
#     is_admin = Column(Boolean, default=False)
#
#     # lazy - не ставить 'dynamic', т.к. ругается pydantic
#     urls = relationship(
#         'URL',
#         back_populates='owner',
#         passive_deletes=True,
#         cascade='all, delete'
#     )
#
#     def __repr__(self):
#         return f'<User: {self.username}>'
#
#     def hash_password(self, password: str):
#         """Метод хеширования пароля."""
#         self.password_hash = password_hasher.hash(password)
#
#     def verify_password(self, password: str):
#         """Метод проверки пароля."""
#         return password_hasher.verify(password, self.password_hash)
#
#
# class URL(Base):
#     """Модель сокращаемых URL."""
#     __tablename__ = 'urls'
#
#     id = Column(Integer, primary_key=True, index=True)
#     link = Column(String, index=True, nullable=False)
#     short_url = Column(String, index=True, nullable=False)
#     user_id = Column(GUID, ForeignKey('users.id', ondelete='CASCADE'), nullable=False)
#     title = Column(String(length=128), nullable=False)
#     description = Column(String(length=512))
#
#     owner = relationship('UserTable', back_populates='urls')
#
#     info = relationship(
#         'URLInfo',
#         uselist=False,
#         back_populates='url',
#         passive_deletes=True,
#         cascade='all, delete'
#     )
#
#     def __repr__(self):
#         return f'<URL: {self.short_url}>'
#
#
# class URLInfo(Base):
#     """Модель информации о сокращаемых URL."""
#     __tablename__ = 'urls_info'
#
#     id = Column(Integer, primary_key=True, index=True)
#     url_id = Column(Integer, ForeignKey('urls.id', ondelete='CASCADE'), nullable=False)
#     created_at = Column(Date, default=date.today())
#     updated_at = Column(Date, default=date.today())
#     link_count = Column(Integer, default=0)
#
#     url = relationship('URL', back_populates='info')
#
#
# @event.listens_for(URL, 'after_insert')
# def do_stuff(mapper, connection, target):
#     url_info_table = URLInfo.__table__
#     query = url_info_table.insert()
#     database.execute(query=query, values={'url_id': target.id})
#
#
# # @event.listens_for(URL, 'refresh')
# # def receive_refresh(target, context, attrs):
# #     pass
