import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER, name TEXT)")

cur.execute("INSERT INTO users VALUES (1, 'Илья')")
cur.execute("INSERT INTO users VALUES (1, 'Мурзик')")
cur.execute("INSERT INTO users VALUES (1, 'Бобик')")
conn.commit()

cur.execute("SELECT * FROM users")
print(cur.fetchall())

conn.close()