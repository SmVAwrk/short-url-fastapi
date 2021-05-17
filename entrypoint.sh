#!/bin/bash

# Ожидание полного старта БД
while ! </dev/tcp/db/5432; do sleep 1; done


alembic revision --autogenerate

# Добавление импорта "fastapi_users" в новый файл миграции alembic
sed -i '8s/^/import fastapi_users\n/' $(find alembic/versions -mmin -1 -name *_.py | sort -r | head -n 1)

alembic upgrade head
uvicorn url_shortener_app.main:app --reload --host 0.0.0.0 --port 8080
