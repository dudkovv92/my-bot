class Note:
    def __init__(self, id, text):
        self.id = id
        self.text = text

    def __str__(self):
        return str(self.id) + ". " + self.text

class NotesApp:
    def __init__(self, file):
        self.file = file
        self.notes = []
        self.load()

    def load(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                for line in f:
                    parts = line.strip().split("|", 1)
                    if len(parts) == 2:
                        self.notes.append(Note(int(parts[0]), parts[1]))
        except FileNotFoundError:
            pass

    def save(self):
        with open(self.file, "w", encoding="utf-8") as f:
            for n in self.notes:
                f.write(str(n.id) + "|" + n.text + "\n")

    def add(self, text):
        new_id = 1
        if self.notes:
            new_id = max(n.id for n in self.notes) + 1
        self.notes.append(Note(new_id, text))
        self.save()

    def show(self):
        if not self.notes:
            print("Заметок нет")
            return
        for n in self.notes:
            print(n)

    def delete(self, note_id):
        self.notes = [n for n in self.notes if n.id != note_id]
        self.save()

    def find(self, word):
        res = [n for n in self.notes if word.lower() in n.text.lower()]
        return res

# --- Проверка ---
app = NotesApp("notes.txt")

while True:
    print("\n1. Добавить")
    print("2. Показать")
    print("3. Найти")
    print("4. Удалить")
    print("5. Выход")
    choice = input("Выбери: ")

    if choice == "1":
        text = input("Текст: ")
        app.add(text)
    elif choice == "2":
        app.show()
    elif choice == "3":
        word = input("Что ищем: ")
        res = app.find(word)
        if not res:
            print("Ничего не найдено")
        for n in res:
            print(n)
    elif choice == "4":
        try:
            app.delete(int(input("ID: ")))
        except ValueError:
            print("Нужно число")
    elif choice == "5":
        break