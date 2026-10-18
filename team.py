class Team:
    def __init__(self, name):
        self.name = name
        self.players = []

    def add(self, player):
        self.players.append(player)

    def __len__(self):
        return len(self.players)

    def __str__(self):
        return self.name + " (" + str(len(self)) + " игроков)"

t = Team("Динамо")
t.add("Илья")
t.add("Мурзик")
print(len(t))
print(t)