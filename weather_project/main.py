from db import WeatherDB
from api import get_weather

db = WeatherDB("weather.db")
cities = ["Лянтор", "Moscow", "Piter", "Kazan"]

for city in cities:
    get_weather(city, db)

print("--- В базе ---")
for row in db.show():
    print(row)