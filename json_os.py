import json

users = [
    {"name": "Илья", "age": 16},
    {"name": "Мурзик", "age": 3}
]

users.append({"name": "Бобик", "age": 5})

with open("users_data.json", "w", encoding="utf-8") as f:
    json.dump(users, f, ensure_ascii=False, indent=2)

print("Сохранено")

with open("users_data.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded)