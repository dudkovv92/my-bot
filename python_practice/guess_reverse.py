class ReverseGame:
    def __init__(self):
        self.low = 1
        self.high = 100
        self.tries = 0

    def guess(self):
        return (self.low + self.high) // 2

    def update(self, answer):
        self.tries += 1
        mid = self.guess()
        if answer == "больше":
            self.low = mid + 1
        elif answer == "меньше":
            self.high = mid - 1

g = ReverseGame()

print("Загадай число от 1 до 100 и отвечай: больше, меньше, угадал")

while True:
    mid = g.guess()
    print("Твоё число: " + str(mid) + "?")
    ans = input("Ответ: ").lower()

    if ans == "угадал":
        g.tries += 1
        print("Я угадал за " + str(g.tries) + " попыток!")
        break
    else:
        g.update(ans)