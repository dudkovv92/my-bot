from typing import List, Dict, Optional

def greet(name: str) -> str:
    return "Привет, " + name

def sum_list(nums: List[int]) -> int:
    return sum(nums)

def find_user(users: Dict[str, int], name: str) -> Optional[int]:
    return users.get(name)

print(greet("Илья"))
print(sum_list([1, 2, 3]))
print(find_user({"Илья": 16}, "Илья"))
print(find_user({"Илья": 16}, "Мурзик"))