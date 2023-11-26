# app/dependencies/database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://med_care:sadath777@34.135.29.238:5432/med_care_bglr"


engine = create_engine(DATABASE_URL, connect_args={}, future=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db =  SessionLocal()
    try:
        yield db
    finally:
        db.close()