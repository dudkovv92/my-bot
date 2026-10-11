import requests

r = requests.get("https://wttr.in/Лянтор?format=j1")
data = r.json()
print(data["current_condition"][0])