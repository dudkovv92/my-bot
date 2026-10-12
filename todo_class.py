class TodoBot:
    def __init__(self, file):
        self.file = file

    def add(self, task):
        with open(self.file, "a", encoding="utf-8") as f:
            f.write(task + "\n")

    def show(self):
        with open(self.file, "r", encoding="utf-8") as f:
            return f.readlines()

    def clear(self):
        with open(self.file, "w", encoding="utf-8") as f:
            f.write("")

    def count(self):
        return len(self.show())

    def find(self, word):
        result = []
        for task in self.show():
            if word in task:
                result.append(task.strip())
        return result

t = TodoBot("todo_class.txt")
t.add("купить хлеб")
t.add("позвонить маме")
print(t.show())
print(t.count())
print(t.find("хлеб"))