from dataclasses import dataclass

@dataclass
class User:
    name: str
    age: int
    email: str
    city: str = "Лянтор"

u = User("Илья", 16, "dfhhfurue@gmail.com")
print(u)
print(u.name, u.age, u.email)