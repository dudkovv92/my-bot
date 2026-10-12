import telebot
import os
from dotenv import load_dotenv
from db import DB

load_dotenv()

class MyBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.db = DB("bot_users.db")

    def set_name(self):
        @self.bot.message_handler(commands=["name"])
        def name_handler(message):
            parts = message.text.split()
            if len(parts) < 2:
                self.bot.send_message(message.chat.id, "Напиши: /name Илья")
                return
            self.db.set_name(message.chat.id, parts[1])
            self.bot.send_message(message.chat.id, "Запомнил: " + parts[1])

    def whoami(self):
        @self.bot.message_handler(commands=["whoami"])
        def whoami_handler(message):
            name = self.db.get_name(message.chat.id)
            if name:
                self.bot.send_message(message.chat.id, "Ты " + name)
            else:
                self.bot.send_message(message.chat.id, "Я тебя не знаю. Напиши /name Имя")

    def run(self):
        self.set_name()
        self.whoami()
        self.bot.polling()

b = MyBot(os.getenv("TOKEN"))
b.run()