import sqlite3

conn = sqlite3.connect
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

cur.execute("INSERT INTO users (name) VALUES ('Илья')")
cur.execute("INSERT INTO users (name) VALUES ('Мурзик')")
cur.execute("INSERT INTO users (name) VALUES ('Бобик')")
conn.commit()

cur.execute("SELECT * FROM users")
print(cur.fetchall())

conn.close()