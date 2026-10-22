import sqlite3

conn = sqlite3.connect("test2.db")
cur = conn.cursor()

cur.execute("DELETE FROM users WHERE name = 'Мурзик'")
cur.execute("DELETE FROM users WHERE id = 2")
conn.commit()

cur.execute("SELECT * FROM users")
print(cur.fetchall())

conn.close()