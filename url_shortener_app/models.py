from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(length=128), unique=True, nullable=False, index=True )
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)

    urls = relationship(
        'URL',
        back_populates='owner',
        lazy='dynamic',
        passive_deletes=True,
        cascade='all, delete'
    )


class URL(Base):
    __tablename__ = 'urls'

    id = Column(Integer, primary_key=True, index=True)
    link = Column(String, index=True)
    short_url = Column(String, index=True)
    user_id = Column(Integer, ForeignKey('users.id', ondelete='CASCADE'))

    user = relationship(
        User,
        back_populates='urls'
    )
