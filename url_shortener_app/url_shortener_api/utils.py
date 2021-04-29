import uuid

from sqlalchemy.orm import Session

from url_shortener_app import models
from url_shortener_app.models import schemas


def get_user_by_id(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email
    )
    db_user.hash_password(user.username)

    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_urls(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.URL).offset(skip).limit(limit).all()


def create_url(db: Session, url: schemas.URLCreate, user_id: int):
    new_path = uuid.uuid4().hex
    db_url = models.URL(**url.dict(), user_id=user_id, short_url=new_path[::4])
    db.add(db_url)
    db.commit()
    db.refresh(db_url)
    return db_url
