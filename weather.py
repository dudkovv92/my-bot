import requests

url = "https://wttr.in/Lyantor?format=j1"
r = requests.get(url)
data = r.json()

temp = data["current_condition"][0]["temp_C"]
hum = data["current_condition"][0]["humidity"]
feel = data["current_condition"][0]["FeelsLikeC"]

print("Температура в Лянторе: " + temp + "°C")
print("Влажность в Лянторе: " + hum + "%")
print("Ощущается как: " + feel + "°C")