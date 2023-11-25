# from pydantic import BaseModel
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# class User(database.Base):
#     id : int
#     username : str
#     email : str
#     contact : str
#     is_delete : bool

#     class Config:
#         orm_mode = True


import datetime as datetime
import sqlalchemy as sqlalchemy


class UserModel(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    password_hash = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow())