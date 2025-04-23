from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.base import Base  # Import Base from the correct location
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def init_db():
    import src.models.user
    import src.models.product
    import src.models.feedback
    Base.metadata.create_all(bind=engine)