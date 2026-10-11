import os
from dotenv import load_dotenv
load_dotenv()

import telebot
from telebot import types
import datetime
import requests

bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, братан!")

@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.send_message(message.chat.id, "Команды: /start, /help, /time, /menu, /weather")

@bot.message_handler(commands=["time"])
def time_cmd(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    bot.send_message(message.chat.id, "Сейчас: " + now)

@bot.message_handler(commands=["menu"])

def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Время"), types.KeyboardButton("Привет"))
    markup.add(types.KeyboardButton("Погода"), types.KeyboardButton("Курс"))
    markup.add(types.KeyboardButton("Факт"))
    bot.send_message(message.chat.id, "Выбери:", reply_markup=markup)

@bot.message_handler(commands=["weather"])
def weather(message):
    r = requests.get("https://wttr.in/Lyantor?format=j1")
    data = r.json()
    temp = data["current_condition"][0]["temp_C"]
    hum = data["current_condition"][0]["humidity"]
    feel = data["current_condition"][0]["FeelsLikeC"]
    text = "Погода в Лянторе:\n"
    text += "Температура: " + temp + "°C\n"
    text += "Влажность: " + hum + "%\n"
    text += "Ощущается как: " + feel + "°C"
    bot.send_message(message.chat.id, text)

@bot.message_handler(func=lambda m: m.text == "Время")
def btn_time(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    bot.send_message(message.chat.id, "Сейчас: " + now)

@bot.message_handler(func=lambda m: m.text == "Привет")
def btn_hi(message):
    bot.send_message(message.chat.id, "И тебе привет, братан!")

@bot.message_handler(commands=["currency"])
def currency(message):
    r = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    data = r.json()
    usd = data["Valute"]["USD"]["Value"]
    eur = data["Valute"]["EUR"]["Value"]
    cny = data["Valute"]["CNY"]["Value"]
    text = "Курс валют:\n"
    text += "USD: " + str(usd) + " ₽\n"
    text += "EUR: " + str(eur) + " ₽\n"
    text += "CNY: " + str(cny) + " ₽"
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["fact"])
def fact(message):
    try:
        r = requests.get("https://api.popcat.xyz/v2/joke")
        data = r.json()
        bot.send_message(message.chat.id, data["message"]["joke"])
    except Exception as e:
        bot.send_message(message.chat.id, "Ошибка: " + str(e))

@bot.message_handler(func=lambda m: m.text == "Погода")
def btn_weather(message):
    weather(message)

@bot.message_handler(func=lambda m: m.text == "Курс")
def btn_currency(message):
    currency(message)

@bot.message_handler(func=lambda m: m.text == "Факт")
def btn_fact(message):
    fact(message)

@bot.message_handler()
def echo(message):
    bot.send_message(message.chat.id, "Ты написал: " + message.text)

bot.polling()