import pytest
from src.api.recommendations import get_recommendations
from src.models.product import Product

@pytest.fixture
def sample_products():
    return [
        Product(id=1, name="Product A", description="Description A", price=10.0, category="Category 1"),
        Product(id=2, name="Product B", description="Description B", price=20.0, category="Category 2"),
        Product(id=3, name="Product C", description="Description C", price=30.0, category="Category 1"),
    ]

def test_get_recommendations_with_valid_input(sample_products):
    user_preferences = {"category": "Category 1"}
    recommendations = get_recommendations(user_preferences)
    
    assert len(recommendations) > 0
    assert all(product.category == "Category 1" for product in recommendations)

def test_get_recommendations_with_no_matching_products(sample_products):
    user_preferences = {"category": "Nonexistent Category"}
    recommendations = get_recommendations(user_preferences)
    
    assert len(recommendations) == 0

def test_get_recommendations_with_empty_preferences(sample_products):
    user_preferences = {}
    recommendations = get_recommendations(user_preferences)
    
    assert len(recommendations) == len(sample_products)  # Assuming it returns all products when no preferences are given

def test_get_recommendations_with_invalid_input(sample_products):
    user_preferences = {"category": None}
    recommendations = get_recommendations(user_preferences)
    
    assert len(recommendations) == 0  # Assuming it returns no products for invalid input