def handle_command(cmd):
    match cmd:
        case "start":
            return "Запуск"
        case "stop":
            return "Стоп"
        case "help":
            return "Помощь"
        case _:
            return "Неизвестная команда"

print(handle_command("start"))
print(handle_command("stop"))
print(handle_command("hello"))