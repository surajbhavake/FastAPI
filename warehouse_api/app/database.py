from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase,Session
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    echo=True #it show whatever happens in terminal and later for production we False it
)

SessoinLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit = False,
)


class Base(DeclarativeBase):
    pass

def get_db():
    db:Session = SessoinLocal()

    try:
        yield db
    finally:
        db.close()


