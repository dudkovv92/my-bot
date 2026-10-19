from functools import reduce

nums = [1, 2, 3, 4, 5]

total = reduce(lambda a, b: a + b, nums)
print(total)

product = reduce(lambda a, b: a * b, nums)
print(product)

words = ["Привет", " ", "мир"]
text = reduce(lambda a, b: a + b, words)
print(text)