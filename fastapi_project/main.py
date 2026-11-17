from fastapi import FastAPI, Request, BackgroundTasks
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import time
from routers import notes, auth

def slow_task(text):
    time.sleep(5)
    print("Фоновая задача выполнена: " + text)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

app.include_router(notes.router)
app.include_router(auth.router)

@app.post("/slow")
def run_slow(background_tasks: BackgroundTasks, text: str = "Тест"):
    background_tasks.add_task(slow_task, text)
    return {"message": "Задача запущена в фоне"}

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    return templates.TemplateResponse(request=request, name="index.html", context={"notes": []})