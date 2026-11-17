from fastapi import FastAPI, Request, BackgroundTasks, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from db import NotesDB, NotesService
from auth import AuthManager, User
import time

def slow_task(text):
    time.sleep(5)
    print("Фоновая задача выполнена: " + text)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
auth = AuthManager()

# --- Настройка сервиса ---
db = NotesDB("notes.db")
service = NotesService(db) # <--- Наш новый сервис

class Note(BaseModel):
    text: str

# --- Фоновые задачи ---
@app.post("/slow")
def run_slow(background_tasks: BackgroundTasks, text: str = "Тест"):
    background_tasks.add_task(slow_task, text)
    return {"message": "Задача запущена в фоне"}

# --- Главная страница (HTML) ---
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"notes": []})

# --- Заметки (через сервис) ---
@app.get("/notes")
def get_notes():
    return service.get_notes() # <--- Обращаемся к сервису

@app.post("/notes")
def add_note(note: Note):
    new_id = service.add_note(note.text) # <--- Обращаемся к сервису
    return {"id": new_id, "text": note.text}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    service.delete_note(note_id) # <--- Обращаемся к сервису
    return {"status": "deleted"}

# --- Авторизация ---
@app.post("/register")
def register(user: User):
    return auth.register(user)

@app.post("/login")
def login(user: User):
    return auth.login(user)

@app.get("/protected")
def protected(username: str = Depends(auth.get_current_user)):
    return {"message": "Привет, " + username + "! Ты в защищённой зоне"}