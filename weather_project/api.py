import requests
import datetime
from db import WeatherDB
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