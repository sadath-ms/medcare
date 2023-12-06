# app/api/v1/user.py
from fastapi import APIRouter, Depends
from medcare_app.schemas import user_schema
from typing import List
from medcare_app.dependencies.database import get_db
from sqlalchemy.orm import Session
from medcare_app.models.user import (
    UserModel
)
from pydantic import parse_obj_as

router = APIRouter()

@router.post("/create-user", response_model=user_schema.UserList)
def create_user(user: user_schema.CreateUser, db:Session=Depends(get_db)):
    # Convert Pydantic model to SQLAlchemy model
    create_user = UserModel(**user.dict())
    # Add the new pandemic record to the database
    db.add(create_user)
    db.commit()
    db.refresh(create_user)
    return {'msg': "successfully created"}

@router.get("/", response_model=user_schema.UserList)
def read_root(db: Session = Depends(get_db)):
    records = db.query(UserModel).first()
    return user_schema.UserList(id=records.id, email=records.email)


