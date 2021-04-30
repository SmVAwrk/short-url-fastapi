"""
Вспомогательные инструменты, необходимые для аутентификации и регистрации
"""

# import os
# import sys
# from datetime import timedelta, datetime
# from typing import Optional
#
# from fastapi import Depends, HTTPException
# from fastapi.security import OAuth2PasswordBearer
# from jose import jwt, JWTError
# from sqlalchemy.orm import Session
# from starlette import status
#
# from .models import User
# from .schemas import TokenData, UserCreate
# from ..db.services import get_db
#
# # Нормализация импортов
# current_path = os.path.dirname(os.path.abspath(__file__))
# ROOT_PATH = os.path.join(current_path, '..')
# sys.path.append(ROOT_PATH)
#
# # Секретный ключ для JWT
# SECRET_KEY = '26ebaf0dfd26a223e987fa5b2d0f8667d9bbb050d872a7a316b08fe8ecfa01a3'
#
# # Алгоритм шифрования
# ALGORITHM = "HS256"
#
# # Длительность действия токена
# ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24
#
# # Объявление URL для получения токена
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')
#
#
# def create_user(db: Session, user: UserCreate):
#     """Вспомогательная функция для создания пользователя."""
#     db_user = User(
#         username=user.username,
#         email=user.email
#     )
#     db_user.hash_password(user.password)
#     db.add(db_user)
#     db.commit()
#     db.refresh(db_user)
#     return db_user
#
#
# def get_user_by_username(db: Session, username: str):
#     """Вспомогательная функция для получения пользователя."""
#     user = db.query(User).filter(User.username == username).first()
#     return user
#
#
# def authenticate_user(db: Session, username: str, password: str):
#     """Вспомогательная функция для аутентификации пользователя."""
#     user = get_user_by_username(db, username)
#     if not user:
#         return False
#     if not user.verify_password(password):
#         return False
#     return user
#
#
# def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
#     """Вспомогательная функция для создания JWT."""
#     to_encode = data.copy()
#     if expires_delta:
#         expire = datetime.utcnow() + expires_delta
#     else:
#         expire = datetime.utcnow() + timedelta(minutes=15)
#     to_encode.update({'exp': expire})
#     encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
#     return encoded_jwt
#
#
# async def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
#     """Функция для получения текущего пользователя по токену."""
#     credentials_exception = HTTPException(
#         status_code=status.HTTP_401_UNAUTHORIZED,
#         detail='Could not validate credentials',
#         headers={'WWW-Authenticate': 'Bearer'},
#     )
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         username: str = payload.get('sub')
#         if username is None:
#             raise credentials_exception
#         token_data = TokenData(username=username)
#     except JWTError:
#         raise credentials_exception
#     user = get_user_by_username(db=db, username=token_data.username)
#     if user is None:
#         raise credentials_exception
#     return user
#
#
# async def get_current_active_user(current_user: User = Depends(get_current_user)):
#     """Функция для проверки, является ли пользователь активированным."""
#     if not current_user.is_active:
#         raise HTTPException(status_code=400, detail='Inactive user')
#     return current_user
