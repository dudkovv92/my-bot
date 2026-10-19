import weakref

class User:
    def __init__(self, name):
        self.name = name

u = User("Илья")
r = weakref.ref(u)

print(r())
print(r() is u)

del u
print(r())