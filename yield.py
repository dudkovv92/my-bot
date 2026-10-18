def evens(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for x in evens(10):
    print(x)