# filepath: test_llm_engine.py
import sys
import os

# Add the src directory to the Python path
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from src.services.llm_engine import get_recommendations

user_preferences = "I like affordable and durable electronics."
product_descriptions = [
    "Smartphone with a long-lasting battery",
    "Budget-friendly laptop",
    "High-end gaming console",
]

recommendations = get_recommendations(user_preferences, product_descriptions)
print("Recommendations:", recommendations)