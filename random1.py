import random
import string

chars = string.ascii_letters + string.digits

for i in range(10):
    password = "".join(random.choice(chars) for _ in range(8))
    print(password)