class MyBot:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print("Привет, я " + self.name)

    def echo(self, text):
        print("Ты написал: " + text)

b = MyBot("Илья")
b.hello()
b.echo("ку")