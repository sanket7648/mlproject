# filepath: src/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.services.database import Base

class User(Base):
    __tablename__ = "users"
    __table_args__ = {"schema": "my_schema"}  # Specify the schema

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    feedbacks = relationship("Feedback", back_populates="user")