from collections import Counter, defaultdict, deque

# Counter — считает элементы
words = ["кот", "собака", "кот", "хомяк", "кот"]
c = Counter(words)
print(c)
print(c.most_common(1))

print("---")

# defaultdict — словарь с дефолтом
d = defaultdict(int)
d["яблоки"] += 1
d["бананы"] += 2
print(d)

print("---")

# deque — быстрая очередь
q = deque([1, 2, 3])
q.appendleft(0)
q.append(4)
print(q)