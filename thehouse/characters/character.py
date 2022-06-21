import random

from thehouse.helpers import print_pause


class Character:
    def __init__(self):
        self.max_health = random.randint(5, 10)
        self.health = self.max_health

    @property
    def is_alive(self):
        """Returns whether the character is alive or not
        Returns boolean
        """
        return True if self.health > 0 else False

    def lose_health(self, damage=1):
        """The character lose health
        :param damage: the amount of damage as integer the character takes
        """
        self.health -= damage
        self.print_health()

    def restore_health(self):
        """Restore the health to the maximum health of the character"""
        self.health = self.max_health
        self.print_health()

    def print_health(self):
        """Prints a bar with the current health"""
        health = "*" * self.health
        pt_lost = "-" * (self.max_health - self.health)
        print_pause(f"Health: {health}{pt_lost}")
