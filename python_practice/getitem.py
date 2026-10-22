class MyList:
    def __init__(self):
        self.items = []

    def add(self, x):
        self.items.append(x)

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

lst = MyList()
lst.add("Илья")
lst.add("Мурзик")

print(lst[0])
print(lst[1])
print(len(lst))
for x in lst:
    print(x)