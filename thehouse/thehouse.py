import rooms


class TheHouse:
    def __init__(self, player):
        self.player = player
        self.rooms = {
            "studio": rooms.Studio(self.player),
        }

    def play_game(self):
        while self.player.health > 0:
            print(self.player.health)
            self.rooms["studio"].intro()
