from fastapi import APIRouter
from fastapi_users import fastapi_users

from .fastapi_auth.services import jwt_authentication
from .auth import endpoints
from .url_shortener_api import api
from .fastapi_auth import routes as auth

routes = APIRouter()

routes.include_router(api.router, prefix='/api/v1')
routes.include_router(auth.router)
# routes.include_router(endpoints.router, prefix='/auth')
