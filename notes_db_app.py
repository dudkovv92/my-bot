import sqlite3

class NotesDB:
    def find(self, word):
        self.cur.execute("SELECT * FROM notes WHERE text LIKE ?", ("%" + word + "%",))
        return self.cur.fetchall()
    
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY,
                text TEXT
            )
        """)
        self.conn.commit()

    def add(self, text):
        self.cur.execute("INSERT INTO notes (text) VALUES (?)", (text,))
        self.conn.commit()

    def show(self):
        self.cur.execute("SELECT * FROM notes")
        return self.cur.fetchall()

    def delete(self, note_id):
        self.cur.execute("DELETE FROM notes WHERE id = ?", (note_id,))
        self.conn.commit()

db = NotesDB("notes_db.db")

while True:
    print("\n1. Добавить")
    print("2. Показать")
    print("3. Удалить")
    print("4. Найти")
    print("5. Выход")
    choice = input("Выбери: ")

    if choice == "1":
        text = input("Текст: ")
        db.add(text)
    elif choice == "2":
        notes = db.show()
        if not notes:
            print("Заметок нет")
        for n in notes:
            print(str(n[0]) + ". " + n[1])
    elif choice == "3":
        try:
            db.delete(int(input("ID: ")))
        except ValueError:
            print("Нужно число")
    elif choice == "4":
        word = input("Что ищем: ")
        res = db.find(word)
        if not res:
            print("Ничего не найдено")
        for n in res:
            print(str(n[0]) + ". " + n[1])
    elif choice == "5":
        break