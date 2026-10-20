from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Note(BaseModel):
    text: str

notes = []
next_id = 1

@app.get("/")
def root():
    return {"message": "Привет, братан!"}

@app.get("/weather")
def weather(city: str = "Лянтор"):
    return {"city": city, "temp": "0°C"}

@app.get("/notes")
def get_notes():
    return notes

@app.post("/notes")
def add_note(note: Note):
    global next_id
    new_note = {"id": next_id, "text": note.text}
    notes.append(new_note)
    next_id += 1
    return new_note

@app.put("/notes/{note_id}")
def update_note(note_id: int, note: Note):
    for n in notes:
        if n["id"] == note_id:
            n["text"] = note.text
            return {"status": "updated", "note": n}
    return {"error": "not found"}

@app.delete("/notes/{note_id}")
def delete_note(note_id: int):
    global notes
    notes = [n for n in notes if n["id"] != note_id]
    return {"status": "deleted"}