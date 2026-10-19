import itertools

# Все пары из двух списков
colors = ["красный", "синий"]
sizes = ["S", "M"]
for c, s in itertools.product(colors, sizes):
    print(c, s)

print("---")

# Комбинации (порядок не важен)
for combo in itertools.combinations([1, 2, 3], 2):
    print(combo)

print("---")

# Перестановки (порядок важен)
for perm in itertools.permutations([1, 2, 3], 2):
    print(perm)