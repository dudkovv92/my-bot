class User:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

u = User("Илья", 16)
print(u.name, u.age)

try:
    u.city = "Лянтор"
except AttributeError as e:
    print("Ошибка:", e)