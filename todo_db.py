import sqlite3

class TodoDB:
    def __init__(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, task TEXT)")
        self.conn.commit()

    def add(self, task):
        self.cur.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        self.conn.commit()

    def show(self):
        self.cur.execute("SELECT * FROM tasks")
        return self.cur.fetchall()

    def done(self, id):
        self.cur.execute("DELETE FROM tasks WHERE id = ?", (id,))
        self.conn.commit()

t = TodoDB("todo.db")
t.add("купить хлеб")
t.add("позвонить маме")
print(t.show())
t.done(1)
print(t.show())