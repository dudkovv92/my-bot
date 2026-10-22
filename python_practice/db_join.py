import sqlite3

conn = sqlite3.connect("join.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
cur.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, user_id INTEGER, task TEXT)")

cur.execute("INSERT INTO users (name) VALUES ('Илья')")
cur.execute("INSERT INTO users (name) VALUES ('Мурзик')")

cur.execute("INSERT INTO tasks (user_id, task) VALUES (1, 'купить хлеб')")
cur.execute("INSERT INTO tasks (user_id, task) VALUES (1, 'позвонить маме')")
cur.execute("INSERT INTO tasks (user_id, task) VALUES (2, 'поспать')")
conn.commit()

cur.execute("SELECT * FROM tasks")
print(cur.fetchall())
cur.execute("""
    SELECT users.name, tasks.task
    FROM tasks
    JOIN users ON tasks.user_id = users.id
    WHERE tasks.user_id = 1
""")
print(cur.fetchall())
conn.close()