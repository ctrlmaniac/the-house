from helpers import print_pause
from .room import Room


class Livingroom(Room):
    def __init__(self, player, thehouse):
        super().__init__(player, thehouse)

    def center(self):
        print_pause("You're in the livingroom!")

        self.move()
