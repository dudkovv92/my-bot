import telebot
import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

class MyBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.conn = sqlite3.connect("bot_users.db", check_same_thread=False)
        self.cur = self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
        self.conn.commit()

    def set_name(self):
        @self.bot.message_handler(commands=["name"])
        def name_handler(message):
            parts = message.text.split()
            if len(parts) < 2:
                self.bot.send_message(message.chat.id, "Напиши: /name Илья")
                return
            self.cur.execute("INSERT OR REPLACE INTO users (id, name) VALUES (?, ?)", (message.chat.id, parts[1]))
            self.conn.commit()
            self.bot.send_message(message.chat.id, "Запомнил: " + parts[1])

    def whoami(self):
        @self.bot.message_handler(commands=["whoami"])
        def whoami_handler(message):
            self.cur.execute("SELECT name FROM users WHERE id = ?", (message.chat.id,))
            row = self.cur.fetchone()
            if row:
                self.bot.send_message(message.chat.id, "Ты " + row[0])
            else:
                self.bot.send_message(message.chat.id, "Я тебя не знаю. Напиши /name Имя")

    def run(self):
        self.set_name()
        self.whoami()
        self.bot.polling()

b = MyBot(os.getenv("TOKEN"))
b.run()