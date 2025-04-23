# filepath: src/services/feedback_service.py
from sqlalchemy.orm import Session
from src.models.feedback import Feedback
from src.services.database import SessionLocal

def save_feedback(user_id: int, product_id: int, feedback_text: str):
    """
    Save user feedback to the database.

    Args:
        user_id (int): The ID of the user providing feedback.
        product_id (int): The ID of the product being reviewed.
        feedback_text (str): The feedback text.

    Returns:
        Feedback: The created feedback entry.
    """
    session: Session = SessionLocal()
    try:
        feedback = Feedback(
            user_id=user_id,
            product_id=product_id,
            feedback_text=feedback_text,
        )
        session.add(feedback)
        session.commit()
        session.refresh(feedback)  # Refresh to get the auto-generated ID
        return feedback
    except Exception as e:
        session.rollback()
        raise Exception(f"Error saving feedback: {e}")
    finally:
        session.close()