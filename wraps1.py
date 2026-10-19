from functools import wraps

def log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Вызов: " + func.__name__)
        return func(*args, **kwargs)
    return wrapper

@log
def add(a, b):
    """Складывает два числа"""
    return a + b

print(add(2, 3))
print(add.__name__)
print(add.__doc__)