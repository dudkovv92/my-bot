class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " ест")

class Dog(Animal):
    def bark(self):
        print(self.name + " говорит: Гав!")

class Cat(Animal):
    def meow(self):
        print(self.name + " говорит: Мяу!")

dog = Dog("Бобик")
cat = Cat("Мурзик")

dog.eat()
dog.bark()
cat.eat()
cat.meow()