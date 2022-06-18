import rooms


class TheHouse:
    def __init__(self, player):
        self.player = player
        self.rooms = {
            "studio": rooms.Studio(self.player),
        }

    def play_game(self):
        while self.player.is_alive():
            self.rooms["studio"].intro()
