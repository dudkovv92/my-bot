import re

text = "Илья и Мурзик пошли в Лянтор"
words = re.findall(r"[А-ЯЁ]\w*", text)
print(words)