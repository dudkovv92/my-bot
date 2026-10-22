class Dog:
    def __init__(self, name):
        self.name = name

    def bark(self):
        print(self.name + " говорит: Гав!")

dog = Dog("Бобик")
dog.bark()