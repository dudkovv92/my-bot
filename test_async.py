import requests

r = requests.get("https://api.open-meteo.com/v1/forecast?latitude=55.75&longitude=37.61&current_weather=true", timeout=10)
print(r.status_code)
print(r.text[:100])