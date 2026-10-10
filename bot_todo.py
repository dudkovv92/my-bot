import telebot
from telebot import types
import os
from dotenv import load_dotenv

load_dotenv()
bot = telebot.TeleBot(os.getenv("TOKEN"))

def menu():
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("Добавить"), types.KeyboardButton("Список"))
    markup.add(types.KeyboardButton("Очистить"))
    return markup

@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id, "Я todo-бот", reply_markup=menu())

@bot.message_handler(commands=["add"])
def add(message):
    task = message.text.replace("/add", "").strip()
    if not task:
        bot.send_message(message.chat.id, "Напиши дело после /add")
        return
    with open("bot_todo.txt", "a", encoding="utf-8") as f:
        f.write(task + "\n")
    bot.send_message(message.chat.id, "Добавил: " + task)

@bot.message_handler(commands=["list"])
def show(message):
    with open("bot_todo.txt", "r", encoding="utf-8") as f:
        tasks = f.readlines()
    if not tasks:
        bot.send_message(message.chat.id, "Список пуст")
        return
    text = ""
    for i, t in enumerate(tasks, 1):
        text += str(i) + ". " + t
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["done"])
def done(message):
    num = message.text.replace("/done", "").strip()
    with open("bot_todo.txt", "r", encoding="utf-8") as f:
        tasks = f.readlines()
    if not num.isdigit() or int(num) < 1 or int(num) > len(tasks):
        bot.send_message(message.chat.id, "Неверный номер")
        return
    tasks.pop(int(num) - 1)
    with open("bot_todo.txt", "w", encoding="utf-8") as f:
        f.writelines(tasks)
    bot.send_message(message.chat.id, "Удалил")

@bot.message_handler(func=lambda m: m.text == "Список")
def btn_list(message):
    show(message)

@bot.message_handler(func=lambda m: m.text == "Очистить")
def btn_clear(message):
    with open("bot_todo.txt", "w", encoding="utf-8") as f:
        f.write("")
    bot.send_message(message.chat.id, "Очистил")

@bot.message_handler(func=lambda m: m.text == "Добавить")
def btn_add(message):
    bot.send_message(message.chat.id, "Напиши: /add твоё дело")

bot.polling()