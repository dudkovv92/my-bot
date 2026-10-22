def sum_all(*args):
    return sum(args)
def make_dict(**kwargs):
    return kwargs

print(make_dict(name="Илья", age=16))
print(sum_all(1, 2, 3))
print(sum_all(5, 10, 15, 20))

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(key + ": " + str(value))

print_info(name="Илья", age=16, city="Лянтор")