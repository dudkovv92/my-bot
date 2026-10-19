import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.61&current_weather=true"
r = requests.get(url, timeout=30)
print(r.status_code)
print(r.json())