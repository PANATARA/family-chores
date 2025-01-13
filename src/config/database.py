from sqlalchemy import create_engine
from core.models import Base
from models.user import UserBase


DB_URL = 'sqlite:///database.db'
engine = create_engine(DB_URL, echo=True)

def create_db_and_tables() -> None:
	Base.metadata.create_all(engine)