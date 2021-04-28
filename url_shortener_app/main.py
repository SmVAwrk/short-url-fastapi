from fastapi import FastAPI

from .routes import routes

app = FastAPI(debug=True)

app.include_router(routes)

