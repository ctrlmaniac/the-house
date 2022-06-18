from .room import Room


class Diningroom(Room):
    def center(self):
        print("You're in the dining room!")

        self.move()
