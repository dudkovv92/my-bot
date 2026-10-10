import json

data = {"name": "Алекс", "age": 17}
print(data)

with open("data.json", "w") as f:
    json.dump(data, f)

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False)