# filepath: src/services/llm_engine.py
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("LLM_API_KEY")

def get_recommendations(user_preferences, product_descriptions):
    """
    Generate product recommendations based on user preferences and product descriptions.

    Args:
        user_preferences (str): A description of the user's preferences.
        product_descriptions (list): A list of product descriptions.

    Returns:
        list: A list of recommended products.
    """
    try:
        # Example prompt for the LLM
        prompt = f"""
        Based on the following user preferences:
        {user_preferences}

        Recommend the best products from the following list:
        {', '.join(product_descriptions)}
        """

        # Use the new ChatCompletion API with gpt-3.5-turbo or gpt-4
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Replace with "gpt-4" if needed
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            max_tokens=150,
            temperature=0.7,
        )

        # Extract recommendations from the response
        recommendations = response["choices"][0]["message"]["content"].strip().split("\n")
        return recommendations

    except Exception as e:
        print(f"Error generating recommendations: {e}")
        return []