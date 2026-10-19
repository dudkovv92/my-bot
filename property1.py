class User:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if len(value) < 2:
            raise ValueError("Имя слишком короткое")
        self._name = value

u = User("Илья")
print(u.name)

u.name = "Мурзик"
print(u.name)

try:
    u.name = "Я"
except ValueError as e:
    print("Ошибка:", e)