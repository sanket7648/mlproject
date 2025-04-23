import pytest
from fastapi.testclient import TestClient
from src.main import app
from src.models.product import Product
from src.services.database import get_db

client = TestClient(app)

@pytest.fixture
def test_db():
    # Setup code for test database
    db = get_db()
    yield db
    # Teardown code for test database

@pytest.fixture
def sample_product(test_db):
    product = Product(name="Sample Product", description="This is a sample product.", price=19.99, category="Sample Category")
    test_db.add(product)
    test_db.commit()
    return product

def test_search_product_by_name(sample_product):
    response = client.get(f"/search?query={sample_product.name}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["name"] == sample_product.name

def test_search_product_not_found():
    response = client.get("/search?query=NonExistentProduct")
    assert response.status_code == 200
    assert len(response.json()) == 0

def test_search_product_by_category(sample_product):
    response = client.get(f"/search?query={sample_product.category}")
    assert response.status_code == 200
    assert len(response.json()) > 0
    assert response.json()[0]["category"] == sample_product.category