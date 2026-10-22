try:
    x = int("abc")
except ValueError:
    print("Это не число!")

try:
    y = 10 / 0
except ZeroDivisionError:
    print("На ноль делить нельзя!")

try:
    print(undefined_var)
except NameError:
    print("Такой переменной нет!")