import argparse
import requests
import logging

logging.basicConfig(
    filename="weather.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

parser = argparse.ArgumentParser(description="Погода в городе")
parser.add_argument("city", help="Название города")
args = parser.parse_args()

logging.info("Запрос погоды: " + args.city)

try:
    r = requests.get("https://wttr.in/" + args.city + "?format=j1")
    data = r.json()
    temp = data["current_condition"][0]["temp_C"]
    print("В " + args.city + ": " + temp + "°C")
    logging.info("Успех: " + temp + "°C")
except Exception as e:
    print("Ошибка: " + str(e))
    logging.error("Ошибка: " + str(e))