from functools import partial

def power(base, exp):
    return base ** exp

# Фиксируем exp = 2
square = partial(power, exp=2)
print(square(5))
print(square(10))

# Фиксируем exp = 3
cube = partial(power, exp=3)
print(cube(3))