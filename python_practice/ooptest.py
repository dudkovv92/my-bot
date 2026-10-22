class Animal:
    def __init__(self, name):
        self.name = name

class Dog(Animal):
    def bark(self):
        print(self.name + " говорит: Гав!")

dog = Dog("Бобик")
dog.bark()