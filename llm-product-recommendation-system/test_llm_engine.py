# filepath: test_llm_engine.py
from src.services.llm_engine import get_recommendations

user_preferences = "I like affordable and durable electronics."
product_descriptions = [
    "Smartphone with a long-lasting battery",
    "Budget-friendly laptop",
    "High-end gaming console",
]

recommendations = get_recommendations(user_preferences, product_descriptions)
print("Recommendations:", recommendations)