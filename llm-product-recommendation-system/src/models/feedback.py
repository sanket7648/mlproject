from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from src.services.database import Base

class Feedback(Base):
    __tablename__ = "feedback"
    __table_args__ = {"schema": "my_schema"}  # Specify the schema

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("my_schema.users.id"))  # Include schema in ForeignKey
    product_id = Column(Integer, ForeignKey("my_schema.products.id"))  # Include schema in ForeignKey
    feedback_text = Column(String, nullable=False)

    user = relationship("User", back_populates="feedbacks")
    product = relationship("Product", back_populates="feedbacks")