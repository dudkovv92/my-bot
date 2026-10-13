import time

def timer(func):
    def wrapper():
        start = time.time()
        func()
        print("Время: " + str(time.time() - start))
    return wrapper

@timer
def work():
    for i in range(1000000):
        pass

work()