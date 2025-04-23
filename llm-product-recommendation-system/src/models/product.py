from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from src.services.database import Base

class Product(Base):
    __tablename__ = "products"
    __table_args__ = {"schema": "my_schema"}  # Specify the schema

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    description = Column(String)
    feedbacks = relationship("Feedback", back_populates="product")