class Money:
    def __init__(self, rub):
        self.rub = rub

    def __str__(self):
        return str(self.rub) + " ₽"

    def __repr__(self):
        return "Money(" + str(self.rub) + ")"

a = Money(100)
print(a)
print(repr(a))
print([a, a])