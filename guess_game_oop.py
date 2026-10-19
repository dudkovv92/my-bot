import random

class Game:
    def __init__(self):
        self.number = random.randint(1, 100)
        self.tries = 0

    def check(self, guess):
        self.tries += 1
        if guess == self.number:
            return "Угадал! Попыток: " + str(self.tries)
        elif guess < self.number:
            return "Больше"
        else:
            return "Меньше"

g = Game()

while True:
    try:
        guess = int(input("Число: "))
    except ValueError:
        print("Введи число")
        continue

    result = g.check(guess)
    print(result)
    if "Угадал" in result:
        break