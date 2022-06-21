from .character import Character


class Player(Character):
    def __init__(self):
        super().__init__()
        self.escaped = False
        self.items = []

    def escape_the_house(self):
        """Lets the Player escape the house"""
        self.escaped = True

    def pick_an_item(self, item):
        """Picks an item and append it to the list
        :param item: an item as a string
        """
        self.items.append(item)
