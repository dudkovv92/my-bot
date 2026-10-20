from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Привет, братан!"}

def test_add_note():
    response = client.post("/notes", json={"text": "Тестовая заметка"})
    assert response.status_code == 200
    assert response.json()["text"] == "Тестовая заметка"