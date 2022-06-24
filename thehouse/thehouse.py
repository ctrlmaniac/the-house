"""thehouse.

This class wraps all rooms and play the game
"""
from thehouse.helpers import print_pause


class TheHouse:
    """TheHouse."""

    def __init__(self, player):
        """Inizialize class.

        :param player: the instantiated player class.
        """
        self.player = player

    def play(self):
        """Play engine."""
        print_pause("\n\n=== THE HOUSE ===\n\n", 3)

        print_pause("Someone, or something hit you and you faint.")
        print_pause(
            "You hear that this someone or something drags you to someplace.\n", 3
        )
        print_pause("You open your eyes and find yourself lying on the floor.")
        print_pause("Your head is pounding and it hurts.")
        print_pause("With a lot of effort you stand up.")
