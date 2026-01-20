from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)


def test_read_root():
    """Test the root endpoint returns Hello World"""
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}


def test_root_endpoint_method():
    """Test that only GET method is allowed on root endpoint"""
    response = client.post("/")
    assert response.status_code == 405  # Method Not Allowed
