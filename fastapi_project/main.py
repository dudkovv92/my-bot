import datetime
import time
import jwt
from fastapi import FastAPI, BackgroundTasks, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from pydantic import BaseModel
from db import NotesDB

app = FastAPI()
db = NotesDB("notes.db")

SECRET = "super_secret_key"
security = HTTPBearer()
users = {} # Пока в памяти

# --- Модели ---
class Note(BaseModel):
    text: str

class User(BaseModel):
    username: str
    password: str

# --- Фоновые задачи ---
def slow_task(text):
    time.sleep(5)
    print("Фоновая задача выполнена: " + text)

@app.post("/slow")
def run_slow(background_tasks: BackgroundTasks, text: str = "Тест"):
    background_tasks.add_task(slow_task, text)
    return {"message": "Задача запущена в фоне"}

# --- Заметки ---
@app.get("/")
def root():
    return {"message": "Привет, братан!"}

@app.get("/notes")
def get_notes():
    return db.get_all()

@app.post("/notes")
def add_note(note: Note):
    new_id = db.add(note.text)
    return {"id": new_id, "text": note.text}

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):
    db.update(note_id, note.text)
    return {"status": "updated"}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    db.delete(note_id)
    return {"status": "deleted"}

# --- Авторизация ---
def create_token(username: str):
    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1)
    }
    return jwt.encode(payload, SECRET, algorithm="HS256")

def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security)):
    try:
        token = credentials.credentials
        payload = jwt.decode(token, SECRET, algorithms=["HS256"])
        return payload["sub"]
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Токен истёк")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Неверный токен")

@app.post("/register")
def register(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="Пользователь уже есть")
    users[user.username] = user.password
    return {"message": "Зарегистрирован"}

@app.post("/login")
def login(user: User):
    if users.get(user.username) != user.password:
        raise HTTPException(status_code=401, detail="Неверный логин или пароль")
    token = create_token(user.username)
    return {"token": token}

@app.get("/protected")
def protected(username: str = Depends(get_current_user)):
    return {"message": "Привет, " + username + "! Ты в защищённой зоне"}