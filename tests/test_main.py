from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint returns Hello World"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}


def test_root_endpoint_method():
    """Test that only GET method is allowed on root endpoint"""
    response = client.post("/")
    assert response.status_code == 405  # Method Not Allowed


def test_add_two_positive_integers():
    """Test adding two positive integers"""
    response = client.get("/add?a=5&b=3")
    assert response.status_code == 200
    assert response.json() == {"result": 8}


def test_add_positive_and_negative():
    """Test adding positive and negative integers"""
    response = client.get("/add?a=10&b=-5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}


def test_add_two_negative_integers():
    """Test adding two negative integers"""
    response = client.get("/add?a=-3&b=-7")
    assert response.status_code == 200
    assert response.json() == {"result": -10}


def test_add_with_zero():
    """Test adding with zero"""
    response = client.get("/add?a=0&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 5}
