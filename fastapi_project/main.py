from fastapi import FastAPI
from pydantic import BaseModel
from db import NotesDB

app = FastAPI()
db = NotesDB("notes.db")

class Note(BaseModel):
    text: str

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