import requests

r = requests.get("https://api.popcat.xyz/v2/joke")
print(r.json())