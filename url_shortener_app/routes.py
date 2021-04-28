from fastapi import APIRouter

from .auth import endpoints
from .url_shortener_api import api

routes = APIRouter()

routes.include_router(api.router, prefix='/api/v1')
routes.include_router(endpoints.router, prefix='/auth')
