from contextlib import contextmanager
import time

@contextmanager
def timer():
    start = time.time()
    yield
    print("Время: " + str(time.time() - start))

with timer():
    total = sum(range(1000000))
    print("Сумма:", total)