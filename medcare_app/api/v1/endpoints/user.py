# app/api/v1/user.py
from fastapi import APIRouter
# from app.models.user import User

router = APIRouter()

@router.get("/")
def read_root():
    return {"Hello": "Welcome...."}

