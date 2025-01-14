from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

#Models import
from core.models import Base
from models.user import UserBase
from models.family import FamilyBase

load_dotenv()

DB_URL = os.getenv("DATABASE_URL")

if not DB_URL:
    raise ValueError("DATABASE_URL is not set in the environment")

engine = create_engine(DB_URL, echo=True)


SessionLocal = sessionmaker(bind=engine)

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_db_and_tables():
	Base.metadata.create_all(bind=engine)
