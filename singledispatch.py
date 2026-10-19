from functools import singledispatch

@singledispatch
def show(x):
    print("Неизвестный тип:", x)

@show.register(int)
def _(x):
    print("Число:", x)

@show.register(str)
def _(x):
    print("Строка:", x)

@show.register(list)
def _(x):
    print("Список:", x)

show(5)
show("Илья")
show([1, 2, 3])
show(3.14)