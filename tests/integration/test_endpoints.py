
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_tasks():
    response = client.get("/tasks/")
    assert response.status_code == 200
