import datetime

now = datetime.datetime(2026, 1, 1)
print("Сейчас:", now)

# Через 7 дней
week_later = now + datetime.timedelta(days=290)
print("Cколько дней прошло:", week_later)

# Разница
diff = week_later - now
print("Разница:", diff.days, "дней")

# Форматирование
print("Красиво:", now.strftime("%d.%m.%Y %H:%M"))