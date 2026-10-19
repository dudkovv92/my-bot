from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return self.name + " говорит: Гав!"

class Cat(Animal):
    def speak(self):
        return self.name + " говорит: Мяу!"

d = Dog("Бобик")
c = Cat("Мурзик")
print(d.speak())
print(c.speak())

# Попробуем создать просто Animal
try:
    a = Animal("Кто-то")
except TypeError as e:
    print("Ошибка:", e)