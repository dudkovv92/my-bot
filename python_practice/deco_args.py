def log(func):
    def wrapper(*args, **kwargs):
        print("Вызов: " + func.__name__)
        result = func(*args, **kwargs)
        print("Готово")
        return result
    return wrapper

@log
def add(a, b):
    return a + b

print(add(2, 3))