from db import NotesDB, NotesService

# Создаем базу и сервис один раз
db_instance = NotesDB("notes.db")
notes_service = NotesService(db_instance)

# Функция-зависимость для получения сервиса
def get_notes_service():
    return notes_service