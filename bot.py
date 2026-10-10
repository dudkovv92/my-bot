import os
from dotenv import load_dotenv

load_dotenv()

import telebot
from telebot import types
import datetime

bot = telebot.TeleBot(os.getenv("TOKEN"))

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Привет, братан!")

@bot.message_handler(commands=["help"])
def help_cmd(message):
    bot.send_message(message.chat.id, "Команды: /start, /help, /time, /menu")

@bot.message_handler(commands=["time"])
def time_cmd(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    bot.send_message(message.chat.id, "Сейчас: " + now)

@bot.message_handler(commands=["menu"])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Время")
    btn2 = types.KeyboardButton("Привет")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Выбери:", reply_markup=markup)

@bot.message_handler(func=lambda m: m.text == "Время")
def btn_time(message):
    now = datetime.datetime.now().strftime("%H:%M:%S")
    bot.send_message(message.chat.id, "Сейчас: " + now)

@bot.message_handler(func=lambda m: m.text == "Привет")
def btn_hi(message):
    bot.send_message(message.chat.id, "И тебе привет, братан!")

@bot.message_handler()
def echo(message):
    bot.send_message(message.chat.id, "Ты написал: " + message.text)

bot.polling()