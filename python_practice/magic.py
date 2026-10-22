class Money:
    def __sub__(self, other):
        return Money(self.rub - other.rub)
    
    def __init__(self, rub):
        self.rub = rub

    def __str__(self):
        return str(self.rub) + " ₽"

    def __add__(self, other):
        return Money(self.rub + other.rub)

a = Money(100)
b = Money(50)
print(a)
print(a + b)
print(a - b)