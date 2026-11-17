import sqlite3
import datetime

class NotesDB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                text TEXT,
                created_at TEXT
            )
        """)
        self.conn.commit()

    def add(self, text):
        now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        self.cur.execute("INSERT INTO notes (text, created_at) VALUES (?, ?)", (text, now))
        self.conn.commit()
        return self.cur.lastrowid

    def get_all(self):
        self.cur.execute("SELECT id, text, created_at FROM notes")
        return [{"id": r[0], "text": r[1], "created_at": r[2]} for r in self.cur.fetchall()]

    def delete(self, note_id):
        self.cur.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()

# --- Наш новый сервисный слой ---
class NotesService:
    def __init__(self, db):
        self.db = db

    def get_notes(self):
        return self.db.get_all()

    def add_note(self, text):
        return self.db.add(text)

    def delete_note(self, note_id):
        self.db.delete(note_id)