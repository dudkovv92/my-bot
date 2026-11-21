import os
from dotenv import load_dotenv
from db import NotesDB, NotesService
from auth import AuthManager

load_dotenv()

DB_URL = os.getenv("DB_URL", "postgresql://postgres:postgres@localhost:5432/notes_db")

db_instance = NotesDB(DB_URL)
notes_service = NotesService(db_instance)

def get_notes_service():
    return notes_service

auth_manager = AuthManager()
def get_auth_manager():
    return auth_manager