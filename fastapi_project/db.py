import sqlite3

class NotesDB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path, check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                text TEXT
            )
        """)
        self.conn.commit()

    def get_all(self):
        self.cur.execute("SELECT id, text FROM notes")
        return [{"id": r[0], "text": r[1]} for r in self.cur.fetchall()]

    def add(self, text):
        self.cur.execute("INSERT INTO notes (text) VALUES (?)", (text,))
        self.conn.commit()
        return self.cur.lastrowid

    def update(self, note_id, text):
        self.cur.execute("UPDATE notes SET text = ? WHERE id = ?", (text, note_id))
        self.conn.commit()

    def delete(self, note_id):
        self.cur.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()