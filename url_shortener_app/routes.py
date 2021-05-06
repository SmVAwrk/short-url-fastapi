from fastapi import APIRouter

from .auth import routes as auth
from .url_app import routes as shotrify_url

routes = APIRouter()

routes.include_router(auth.router)
routes.include_router(shotrify_url.api_router, prefix='/api/v1')
routes.include_router(shotrify_url.main_router)

