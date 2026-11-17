from fastapi.testclient import TestClient
from main import app

# Создаем тестовый клиент
client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert "Мои заметки" in response.text

def test_add_note():
    response = client.post("/notes", json={"text": "Тестовая заметка для проверки"})
    assert response.status_code == 200
    assert "text" in response.json()

def test_get_notes():
    response = client.get("/notes")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_delete_note():
    # Сначала создаем заметку
    response = client.post("/notes", json={"text": "Заметка на удаление"})
    note_id = response.json()["id"]
    
    # Теперь удаляем ее
    response = client.delete(f"/notes/{note_id}")
    assert response.status_code == 200
    assert response.json() == {"status": "deleted"}