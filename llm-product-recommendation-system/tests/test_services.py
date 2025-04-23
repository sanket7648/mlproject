import pytest
from src.services.database import Database
from src.services.caching import Cache
from src.services.llm_engine import LLMEngine

@pytest.fixture
def db():
    database = Database()
    yield database
    database.close()

@pytest.fixture
def cache():
    cache_instance = Cache()
    yield cache_instance
    cache_instance.clear()

@pytest.fixture
def llm_engine():
    engine = LLMEngine()
    yield engine

def test_database_connection(db):
    assert db.is_connected() is True

def test_create_user(db):
    user_data = {"username": "testuser", "password": "testpass", "email": "test@example.com"}
    user = db.create_user(user_data)
    assert user.username == user_data["username"]

def test_cache_set_get(cache):
    cache.set("key", "value")
    assert cache.get("key") == "value"

def test_llm_engine_recommendation(llm_engine):
    user_input = "I like action movies and sci-fi."
    recommendations = llm_engine.get_recommendations(user_input)
    assert len(recommendations) > 0
    assert all(isinstance(rec, dict) for rec in recommendations)  # Assuming recommendations are dicts

def test_cache_eviction(cache):
    cache.set("key1", "value1")
    cache.set("key2", "value2")
    cache.evict("key1")
    assert cache.get("key1") is None
    assert cache.get("key2") == "value2"