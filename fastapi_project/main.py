from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import time

# Импортируем наши роутеры
from routers import notes, auth

def slow_task(text):
    time.sleep(5)
    print("Фоновая задача выполнена: " + text)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Подключаем роутеры к приложению
app.include_router(notes.router)
app.include_router(auth.router)

# --- Фоновые задачи ---
@app.post("/slow")
def run_slow(background_tasks: BackgroundTasks, text: str = "Тест"):
    background_tasks.add_task(slow_task, text)
    return {"message": "Задача запущена в фоне"}

# --- Главная страница (HTML) ---
@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"notes": []})