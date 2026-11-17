from db import NotesDB, NotesService
from auth import AuthManager

# --- Зависимости для заметок ---
db_instance = NotesDB("notes.db")
notes_service = NotesService(db_instance)

def get_notes_service():
    return notes_service

# --- Зависимости для авторизации ---
auth_manager = AuthManager()

def get_auth_manager():
    return auth_manager