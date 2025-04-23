from fastapi import APIRouter, HTTPException
from src.services.llm_engine import get_recommendations

router = APIRouter()

@router.post("/recommendations/")
async def generate_recommendations(user_preferences: str, product_descriptions: list[str]):
    """
    Generate product recommendations based on user preferences and product descriptions.

    Args:
        user_preferences (str): A description of the user's preferences.
        product_descriptions (list): A list of product descriptions.

    Returns:
        list: A list of recommended products.
    """
    try:
        recommendations = get_recommendations(user_preferences, product_descriptions)
        return {"recommendations": recommendations}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating recommendations: {e}")