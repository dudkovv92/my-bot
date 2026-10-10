name = input("Как тебя зовут? ")
with open("name.txt", "w") as f:
    f.write(name)