# main.py
from fastapi import FastAPI
from app.api.v1 import user as user_apis
from medcare_app.dependencies.database import engine
from medcare_app.models import user as user_models




app = FastAPI(
    title='Medcare APP',
    description='Medical care application',
    version="1.0.0"
)


app.include_router(user_apis.router)
user_models.Base.metadata.create_all(bind=engine)
