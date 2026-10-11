import requests

r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
data = r.json()

usd = data["Valute"]["USD"]["Value"]
eur = data["Valute"]["EUR"]["Value"]
cny = data["Valute"]["CNY"]["Value"]
print("Доллар: " + str(usd) + " ₽")
print("Евро: " + str(eur) + " ₽")
print("Юань: " + str(cny) + " ₽")