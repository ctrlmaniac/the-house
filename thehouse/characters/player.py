from .character import Character


class Player(Character):
    def __init__(self):
        super().__init__()
        self.escaped = False
        self.items = []

    def is_alive(self):
        return True if self.health > 0 else False

    def escape_the_house(self):
        self.escaped = True

    def pick_an_item(self, item):
        self.items.append(item)
