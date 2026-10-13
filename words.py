text = "я учу python и я учу ботов"
words = text.split()
counts = {}

for w in words:
    if w in counts:
        counts[w] += 1
    else:
        counts[w] = 1

print(counts)
for w, c in counts.items():
    if c > 1:
        print(w, c)