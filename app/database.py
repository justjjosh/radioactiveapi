import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

load_dotenv()

Database_URL = os.getenv("DATABASE_URL")
if not Database_URL:
    raise ValueError("DATABASE_URL environment variable is not set.")

engine = create_engine(Database_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#parent class that all other database models will inherit from.
Base = declarative_base()

#dependency that will be injected into FASTAPI routes to get a database session.
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()