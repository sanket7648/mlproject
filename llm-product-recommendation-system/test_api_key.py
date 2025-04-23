import openai
import os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("LLM_API_KEY")

try:
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Test if this API key works."},
        ],
    )
    print("API Key is working!")
    print(response["choices"][0]["message"]["content"])
except Exception as e:
    print(f"Error: {e}")