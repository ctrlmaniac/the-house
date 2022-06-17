import rooms


class TheHouse:
    def __init__(self):
        self.rooms = {
            "studio": rooms.Studio(),
        }

    def play_game(self):
        self.rooms["studio"].intro()
