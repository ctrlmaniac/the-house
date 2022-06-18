from helpers.print_pause import print_pause
from .room import Room


class Kitchen(Room):
    def center(self):
        print_pause("You're in the kitchen!")
        print_pause("On your right there's a door.")
        print_pause("On your left there are some kitchen's drawers")
        print_pause("Backwards there are other kitchen's drawers")
        print_pause("In front of you there's a window")

        self.move()
