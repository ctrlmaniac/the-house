import random

from .character import Character


class Monster(Character):
    def __init__(self, player):
        super().__init__()
        self.player = player

    def __str__(self):
        return f"Monster - health: {self.health}"

    def deals_damage(self):
        """Deals random damage"""
        damage = random.randint(1, 2)

        self.player.loose_health(damage)
