from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List
from src.services.database import save_feedback
from src.models.feedback import Feedback as FeedbackModel

router = APIRouter()

class Feedback(BaseModel):
    user_id: int
    product_id: int
    rating: int
    comments: str

@router.post("/feedback/", response_model=FeedbackModel)
async def submit_feedback(feedback: Feedback):
    try:
        saved_feedback = await save_feedback(feedback)
        return saved_feedback
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/feedback/{user_id}", response_model=List[FeedbackModel])
async def get_user_feedback(user_id: int):
    try:
        feedback_list = await get_feedback_by_user(user_id)
        return feedback_list
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))