# main.py
from fastapi import FastAPI
# from app.api.v1 import user
from medcare_app.api.v1.endpoints import user
from medcare_app.models import Base
from medcare_app.dependencies.database import engine
from medcare_app.dependencies.database import SessionLocal
from sqlalchemy.orm import Session
from medcare_app.models.user import UserModel




app = FastAPI()

# app.include_router(user.router)
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
