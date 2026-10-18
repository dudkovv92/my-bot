names = ["Илья", "Мурзик", "Бобик"]
lengths = [4, 6, 5]

my_dict = {name: length for name, length in zip(names, lengths)}
print(my_dict)

my_dict2 = {name: len(name) for name in names}
print(my_dict2)