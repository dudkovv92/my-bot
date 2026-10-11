class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name + " ест")

class Cat(Animal):
    def meow(self):
        print(self.name + " говорит: Мяу!")

cat = Cat("Родитель Мурзика")
cat.eat()
cat.meow()