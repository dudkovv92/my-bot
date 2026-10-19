def process(data):
    match data:
        case []:
            return "Пустой список"
        case [x]:
            return "Один элемент: " + str(x)
        case [x, y]:
            return "Два элемента: " + str(x) + ", " + str(y)
        case [x, *rest]:
            return "Много: первый " + str(x) + ", остальные " + str(rest)
        case {"name": name}:
            return "Словарь с именем: " + name
        case _:
            return "Неизвестно"

print(process([]))
print(process([5]))
print(process([1, 2]))
print(process([1, 2, 3, 4]))
print(process({"name": "Илья"}))