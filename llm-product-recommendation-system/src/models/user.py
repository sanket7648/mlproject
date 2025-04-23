# filepath: src/models/user.py
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.models.base import Base  # Import Base from the new file

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    feedbacks = relationship("Feedback", back_populates="user")