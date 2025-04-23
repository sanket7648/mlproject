from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from src.services.database import Base, engine
from src.models.user import User
from src.models.product import Product
from src.models.feedback import Feedback

def initialize_database():
    with engine.connect() as connection:
        # Use sqlalchemy.text() to execute raw SQL
        connection.execute(text("CREATE SCHEMA IF NOT EXISTS my_schema;"))  
    print("Creating database tables...")
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully.")

if __name__ == "__main__":
    initialize_database()