matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Разворачиваем в один список
flat = [x for row in matrix for x in row]
print(flat)

# Оставляем только чётные
evens = [x for row in matrix for x in row if x % 2 == 0]
print(evens)