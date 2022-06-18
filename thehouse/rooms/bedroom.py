from helpers.print_pause import print_pause
from .room import Room


class Bedroom(Room):
    def center(self):
        print_pause("You're in the bedroom!")
        print_pause("On your right there's a window.")
        print_pause("On your left there's a door")
        print_pause("Backwards there's a bed.")
        print_pause("In front of you there's a dresser.")

        self.move()
