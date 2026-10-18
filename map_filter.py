nums = [1, 2, 3, 4, 5, 6]
res = map(lambda x: x * x, filter(lambda x: x % 2 != 0, nums))
print(list(res))