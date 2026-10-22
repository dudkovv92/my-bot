import requests

r = requests.get("https://api.github.com/users/dudkovv92")
data = r.json()
print(data["created_at"])
print(data["avatar_url"])