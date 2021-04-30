"""
Модели, связанные с аутентификацией и регистрацией
"""

from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


# class User(Base):
#     __tablename__ = 'users'
#
#     id = Column(Integer, primary_key=True, index=True)
#     username = Column(String(length=128), unique=True, nullable=False, index=True )
#     email = Column(String, unique=True, nullable=False, index=True)
#     password_hash = Column(String, nullable=False)
#     is_active = Column(Boolean, default=False)
#     is_admin = Column(Boolean, default=False)
#     registration_date = Column(Date, default=date.today())
#
#     # lazy - не ставить 'dynamic', т.к. ругается pydantic
#     urls = relationship(
#         URL,
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
#         self.password_hash = pwd_context.hash(password)
#
#     def verify_password(self, password: str):
#         """Метод проверки пароля."""
#         return pwd_context.verify(password, self.password_hash)