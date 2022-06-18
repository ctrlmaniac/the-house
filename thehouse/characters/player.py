import random


class Player:
    def __init__(self):
        self.health = random.randint(5, 10)

    def loose_health(self):
        self.health -= 1

    def is_alive(self):
        while self.health > 0:
            return True
        return False
