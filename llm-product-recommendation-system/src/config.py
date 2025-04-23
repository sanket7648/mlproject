import os

class Config:
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your_secret_key")
    LLM_API_KEY = os.getenv("LLM_API_KEY", "your_llm_api_key")
    CACHE_TIMEOUT = int(os.getenv("CACHE_TIMEOUT", 300))  # in seconds
    DEBUG = os.getenv("DEBUG", "False").lower() in ("true", "1", "t")

config = Config()