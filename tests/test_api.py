from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    
def test_api_endpoint():
    response = client.get("/api/v1")
    assert response.status_code == 404  # Will be 404 as we don't have a specific route for /api/v1

def test_openapi_docs():
    response = client.get("/docs")
    assert response.status_code == 200