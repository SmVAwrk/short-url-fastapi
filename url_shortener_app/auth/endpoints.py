"""
Контроллеры, связанные с аутентификацией и регистрацией.
"""
#
# from fastapi import APIRouter, Depends, HTTPException
# from fastapi.security import OAuth2PasswordRequestForm
# from pydantic.datetime_parse import timedelta
# from sqlalchemy.orm import Session
# from starlette import status
#
# from .schemas import Token, User, UserCreate, InspectUser
# from .services import authenticate_user, ACCESS_TOKEN_EXPIRE_MINUTES, create_access_token, get_current_active_user, \
#     get_user_by_username, create_user
# from db.services import get_db

# # Создание роутера
# router = APIRouter()
#
#
# @router.post("/users/", response_model=User)
# def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
#     db_user = get_user_by_username(db, username=user.username)
#     if db_user:
#         raise HTTPException(status_code=400, detail="Email already registered")
#     return create_user(db=db, user=user)
#
#
# @router.get("/users/me/", response_model=InspectUser)
# async def read_users_me(current_user: User = Depends(get_current_active_user)):
#     """Контроллер для получения информации о своем аккаунте."""
#     return current_user
#
#
# @router.post('/token', response_model=Token)
# async def login_for_access_token(db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
#     """Контроллер для получения токена."""
#     user = authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail='Incorrect username or password',
#             headers={'WWW-Authenticate': 'Bearer'},
#         )
#     access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
#     access_token = create_access_token(
#         data={'sub': user.username}, expires_delta=access_token_expires
#     )
#     return {'access_token': access_token, 'token_type': 'bearer'}
#
#
# @router.get("/users/me/items/")
# async def read_own_items(current_user: User = Depends(get_current_active_user)):
#     return [{"item_id": "Foo", "owner": current_user.username}]

