

import datetime as datetime
import sqlalchemy as sqlalchemy
from medcare_app.dependencies.database import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.INTEGER, primary_key=True, index=True)
    email = sqlalchemy.Column(sqlalchemy.String, unique=True, index=True)
    password_hash = sqlalchemy.Column(sqlalchemy.String)
    created_at = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.utcnow())