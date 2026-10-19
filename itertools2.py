import itertools

# chain — склеить
a = [1, 2]
b = [3, 4]
c = [5]
print(list(itertools.chain(a, b, c)))

# groupby — сгруппировать
words = ["кот", "собака", "кит", "слон", "крот"]
words.sort(key=lambda w: w[0])  # сначала сортируем по первой букве
for letter, group in itertools.groupby(words, key=lambda w: w[0]):
    print(letter, list(group))