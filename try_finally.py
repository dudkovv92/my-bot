try:
    x = 10 / 0
except ZeroDivisionError:
    print("Ошибка")
else:
    print("Всё ок, x =", x)
finally:
    print("Это выполнится всегда")