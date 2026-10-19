from enum import Enum

class Status(Enum):
    NEW = "новая"
    IN_PROGRESS = "в работе"
    DONE = "готово"

print(Status.NEW)
print(Status.NEW.value)
print(Status.NEW.name)

task_status = Status.IN_PROGRESS
if task_status == Status.IN_PROGRESS:
    print("Задача в работе")