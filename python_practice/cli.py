import argparse

parser = argparse.ArgumentParser(description="Моя программа")
parser.add_argument("name", help="Твоё имя")
parser.add_argument("--age", type=int, default=0, help="Твой возраст")
parser.add_argument("--city", default="Лянтор", help="Город")

args = parser.parse_args()

print("Привет, " + args.name)
print("Возраст: " + str(args.age))
print("Город: " + args.city)