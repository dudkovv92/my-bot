tasks = []

with open("todo.txt", "r") as f:
    for line in f:
        tasks.append(line.strip())

while True:
    t = input("Дело (или 'выход'): ")
    if t == "выход":
       break 
    tasks.append(t) 

with open("todo.txt", "w") as f:
    for t in tasks:
        f.write(t + "\n")

print(tasks)