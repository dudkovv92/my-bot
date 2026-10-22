tasks = []

with open("todo.txt", "r") as f:
    for line in f:
        tasks.append(line.strip())

print(tasks)