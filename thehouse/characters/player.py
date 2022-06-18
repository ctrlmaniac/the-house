import random

from helpers.print_pause import print_pause


class Player:
    def __init__(self):
        self.max_health = random.randint(5, 10)
        self.health = self.max_health

    def loose_health(self):
        self.health -= 1
        health = "*" * self.health
        pt_lost = "-" * (self.max_health - self.health)
        print_pause(f"Health: {health}{pt_lost}")