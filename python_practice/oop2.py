class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(self.name + " говорит: Мяу! Мне " + str(self.age) + " лет")

cat1 = Cat("Мурзик", 3)
cat2 = Cat("Барсик", 5)

cat1.meow()
cat2.meow()