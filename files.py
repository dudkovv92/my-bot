import os

if os.path.exists("test_folder"):
    os.rmdir("test_folder")
    print("Удалено")
else:
    print("Нет такой папки")