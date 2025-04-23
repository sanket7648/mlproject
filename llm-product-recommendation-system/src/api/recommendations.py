from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.services.llm_engine import get_recommendations
from services.database import get_user_preferences

router = APIRouter()

class RecommendationRequest(BaseModel):
    user_id: int

class RecommendationResponse(BaseModel):
    recommendations: list

@router.post("/recommendations", response_model=RecommendationResponse)
async def generate_recommendations(request: RecommendationRequest):
    user_preferences = await get_user_preferences(request.user_id)
    if not user_preferences:
        raise HTTPException(status_code=404, detail="User preferences not found")
    
    recommendations = await get_recommendations(user_preferences)
    return RecommendationResponse(recommendations=recommendations)