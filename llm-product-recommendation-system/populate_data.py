# filepath: populate_data.py
from sqlalchemy.orm import Session
from src.services.database import SessionLocal
from src.models.product import Product
from src.models.user import User

def populate_data():
    session: Session = SessionLocal()
    try:
        # Add sample products
        products = [
            Product(name="Product 1", description="Description for product 1"),
            Product(name="Product 2", description="Description for product 2"),
        ]
        session.add_all(products)

        # Add sample users
        users = [
            User(username="user1", email="user1@example.com"),
            User(username="user2", email="user2@example.com"),
        ]
        session.add_all(users)

        session.commit()
        print("Sample data added successfully.")
    except Exception as e:
        session.rollback()
        print(f"Error: {e}")
    finally:
        session.close()

if __name__ == "__main__":
    populate_data()