class Money:
    def __lt__(self, other):
        return self.rub < other.rub
    
    def __init__(self, rub):
        self.rub = rub

    def __eq__(self, other):
        return self.rub == other.rub

a = Money(100)
b = Money(100)
c = Money(50)

print(a == b)
print(a == c)
print(c < a)