from fastapi import APIRouter, Depends
from pydantic import BaseModel
from dependencies import get_notes_service
from db import NotesService

router = APIRouter()

class Note(BaseModel):
    text: str

@router.get("/notes")
def get_notes(service: NotesService = Depends(get_notes_service)):
    return service.get_notes()

@router.post("/notes")
def add_note(note: Note, service: NotesService = Depends(get_notes_service)):
    new_id = service.add_note(note.text)
    return {"id": new_id, "text": note.text}

@router.delete("/notes/{note_id}")
def delete_note(note_id: int, service: NotesService = Depends(get_notes_service)):
    service.delete_note(note_id)
    return {"status": "deleted"}