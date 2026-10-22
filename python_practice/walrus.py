# Без walrus
data = input("Введи: ")
if data:
    print("Ты ввёл: " + data)

# С walrus (короче)
if (data := input("Введи: ")):
    print("Ты ввёл: " + data)