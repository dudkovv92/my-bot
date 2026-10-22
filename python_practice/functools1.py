import time
from functools import lru_cache

# Без кеша
def fib_slow(n):
    if n <= 1:
        return n
    return fib_slow(n - 1) + fib_slow(n - 2)

# С кешем
@lru_cache(maxsize=None)
def fib_fast(n):
    if n <= 1:
        return n
    return fib_fast(n - 1) + fib_fast(n - 2)

start = time.time()
print("Без кеша:", fib_slow(30))
print("Время:", time.time() - start)

start = time.time()
print("С кешем:", fib_fast(30))
print("Время:", time.time() - start)