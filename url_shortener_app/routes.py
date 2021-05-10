from fastapi import APIRouter

from .auth import routes as auth
from .url_app import routes as shotrify_url

# Создание общего роута
routes = APIRouter()

# Подключение роутов всех приложений к одному общему
routes.include_router(auth.router)
routes.include_router(shotrify_url.api_router, prefix='/api/v1')
routes.include_router(shotrify_url.main_router)

