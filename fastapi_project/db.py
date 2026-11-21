import psycopg2
import datetime
from psycopg2.extras import RealDictCursor

class NotesDB:
    def __init__(self, db_url):
        # db_url — это строка подключения к базе (например, postgresql://user:pass@localhost/db)
        self.conn = psycopg2.connect(db_url, cursor_factory=RealDictCursor)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id SERIAL PRIMARY KEY,
                text TEXT,
                created_at TEXT
            )
        """)
        self.conn.commit()

    def add(self, text):
        now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")
        self.cur.execute("INSERT INTO notes (text, created_at) VALUES (%s, %s) RETURNING id", (text, now))
        new_id = self.cur.fetchone()["id"]
        self.conn.commit()
        return new_id

    def get_all(self):
        self.cur.execute("SELECT id, text, created_at FROM notes")
        return self.cur.fetchall()

    def update(self, note_id, text):
        self.cur.execute("UPDATE notes SET text = %s WHERE id = %s", (text, note_id))
        self.conn.commit()

    def delete(self, note_id):
        self.cur.execute("DELETE FROM notes WHERE id = %s", (note_id,))
        self.conn.commit()

class NotesService:
    def __init__(self, db):
        self.db = db

    def get_notes(self):
        return self.db.get_all()

    def add_note(self, text):
        return self.db.add(text)

    def update_note(self, note_id, text):
        self.db.update(note_id, text)

    def delete_note(self, note_id):
        self.db.delete(note_id)