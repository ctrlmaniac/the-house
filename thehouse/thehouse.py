import rooms

from helpers import random_death


class TheHouse:
    def __init__(self, player):
        self.player = player
        self.rooms = {
            "studio": rooms.Studio(self.player),
        }

    def play_game(self):
        while not self.player.escaped or self.player.is_alive():
            self.rooms["studio"].intro()

            if not self.player.is_alive():
                random_death()
                break

            if self.player.escaped:
                print("Congratulations! You beat the game!")
                break
