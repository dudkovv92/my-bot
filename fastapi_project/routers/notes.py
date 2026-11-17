from fastapi import APIRouter
from pydantic import BaseModel
from db import NotesDB, NotesService

router = APIRouter()

db = NotesDB("notes.db")
service = NotesService(db)

class Note(BaseModel):
    text: str

@router.get("/notes")
def get_notes():
    return service.get_notes()

@router.post("/notes")
def add_note(note: Note):
    new_id = service.add_note(note.text)
    return {"id": new_id, "text": note.text}

@router.delete("/notes/{note_id}")
def delete_note(note_id: int):
    service.delete_note(note_id)
    return {"status": "deleted"}