# 📝 Notes App (FastAPI + PostgreSQL + Docker)

Приложение для заметок с полноценным CRUD-функционалом, темной темой и современной архитектурой.

## 🚀 Стек технологий
* **Backend:** Python, FastAPI
* **Database:** PostgreSQL (SQLAlchemy, psycopg2)
* **Frontend:** HTML, CSS, JavaScript (Fetch API)
* **Инструменты:** Docker, Docker Compose, Pytest, Git

## ⚙️ Как запустить
1. Клонируйте репозиторий.
2. Убедитесь, что у вас установлен Docker Desktop.
3. В терминале выполните команду:
```bash
docker-compose up --build

4.Откройте в браузере: http://127.0.0.1:8000

📋 Функционал
Создание заметок

Просмотр списка заметок

Редактирование заметок

Удаление заметок

Автоматическая документация API (Swagger UI): http://127.0.0.1:8000/docs

📂 Архитектура
main.py — точка входа

routers/ — эндпоинты (auth, notes)

dependencies.py — внедрение зависимостей

db.py — работа с базой данных

auth.py — JWT-авторизация

templates/ — HTML-шаблоны

tests/ — тесты (pytest)
