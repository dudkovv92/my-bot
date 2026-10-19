import sqlite3

class WeatherDB:
    def __init__(self, path):
        self.conn = sqlite3.connect(path)
        self.cur = self.conn.cursor()
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS weather (
                id INTEGER PRIMARY KEY,
                city TEXT,
                temp TEXT,
                time TEXT
            )
        """)
        self.conn.commit()

    def save(self, city, temp, time):
        self.cur.execute(
            "INSERT INTO weather (city, temp, time) VALUES (?, ?, ?)",
            (city, temp, time)
        )
        self.conn.commit()

    def show(self):
        self.cur.execute("SELECT * FROM weather")
        return self.cur.fetchall()