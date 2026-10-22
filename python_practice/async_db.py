import requests
import sqlite3
import datetime

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

def get_weather(city, db):
    coords = {
        "Лянтор": (61.62, 72.17),
        "Moscow": (55.75, 37.61),
        "Piter": (59.93, 30.31),
        "Kazan": (55.79, 49.12)
    }
    lat, lon = coords[city]
    url = "https://api.open-meteo.com/v1/forecast?latitude=" + str(lat) + "&longitude=" + str(lon) + "&current_weather=true"
    
    try:
        r = requests.get(url, timeout=30)
        data = r.json()
        temp = str(data["current_weather"]["temperature"])
        now = datetime.datetime.now().strftime("%H:%M:%S")
        db.save(city, temp, now)
        print(city + ": " + temp + "°C")
    except Exception as e:
        print(city + " — " + type(e).__name__)

db = WeatherDB("weather_sync.db")
cities = ["Лянтор", "Moscow", "Piter", "Kazan"]

for city in cities:
    get_weather(city, db)

print("--- В базе ---")
for row in db.show():
    print(row)