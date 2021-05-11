from logging import config as log_config, getLogger
import traceback

from fastapi import FastAPI
from starlette import status
from starlette.requests import Request
from starlette.responses import JSONResponse

from .core.config import DEBUG, LOGGING_CONFIG
from .core.db.database import database
from .routes import routes

log_config.dictConfig(LOGGING_CONFIG)
logger = getLogger(__name__)

# Создание приложения FastAPI
app = FastAPI(debug=DEBUG)

# Подключение роутов к приложению
app.include_router(routes)


@app.exception_handler(500)
def error_handler(request: Request, exc):
    """Обработчик 500-ой ошибки при отключенном DEBUG-режиме."""
    logger.error(f'Ошибка: {exc.__repr__()}\nTraceback: {traceback.format_tb(exc.__traceback__)}')
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={'message': 'Invalid request'},
    )


@app.on_event('startup')
async def startup():
    """Событие для подключения к БД при начале обработки запроса."""
    await database.connect()


@app.on_event('shutdown')
async def shutdown():
    """Событие для отключения после обработки запроса."""
    await database.disconnect()

