from fastapi import APIRouter
from fastapi_users import fastapi_users

from .auth.services import jwt_authentication
from .old_auth import endpoints
from .url_shortener_api import api
from .auth import routes as auth
from .url_app import routes as shotrify_url

routes = APIRouter()

# routes.include_router(api.router, prefix='/api/v1')
routes.include_router(auth.router)
routes.include_router(shotrify_url.router, prefix='/api/v1')

