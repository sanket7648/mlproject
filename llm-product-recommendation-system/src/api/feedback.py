from fastapi import APIRouter, HTTPException
from src.services.feedback_service import save_feedback  # Updated import
from src.models.feedback import FeedbackModel

router = APIRouter()

@router.post("/feedback/", response_model=FeedbackModel)
async def create_feedback(user_id: int, product_id: int, feedback_text: str):
    """
    Create a new feedback entry.

    Args:
        user_id (int): The ID of the user providing feedback.
        product_id (int): The ID of the product being reviewed.
        feedback_text (str): The feedback text.

    Returns:
        FeedbackModel: The created feedback entry.
    """
    try:
        feedback = save_feedback(user_id, product_id, feedback_text)
        return feedback
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving feedback: {e}")