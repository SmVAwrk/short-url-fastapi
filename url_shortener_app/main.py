from typing import List

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from url_shortener_app import models, schemas, utils
from url_shortener_app.database import engine, SessionLocal


app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = utils.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return utils.create_user(db=db, user=user)


@app.get("/users/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = utils.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/users/{user_id}/urls/", response_model=schemas.URL)
def create_item_for_user(
    user_id: int, url: schemas.URLCreate, db: Session = Depends(get_db)
):
    return utils.create_url(db=db, url=url, user_id=user_id)
