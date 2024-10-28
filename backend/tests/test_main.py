
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_task():
    response = client.post("/tasks/", json={"title": "Test Task", "description": "Description", "deadline": "2023-12-31T23:59:59"})
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
