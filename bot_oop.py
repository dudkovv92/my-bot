import telebot
import os
from dotenv import load_dotenv

load_dotenv()

class MyBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)

    def start(self):
        @self.bot.message_handler(commands=["start"])
        def start(message):
            self.bot.send_message(message.chat.id, "Привет из класса!")

    def help_cmd(self):
        @self.bot.message_handler(commands=["help"])
        def help_handler(message):
            self.bot.send_message(message.chat.id, "Команды: /start, /help")

    def echo(self):
        @self.bot.message_handler()
        def echo_handler(message):
            self.bot.send_message(message.chat.id, "Ты написал: " + message.text)

    def run(self):
        self.start()
        self.help_cmd()
        self.echo()
        self.bot.polling()

b = MyBot(os.getenv("TOKEN"))
b.run()