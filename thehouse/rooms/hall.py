from helpers import print_pause

from .room import Room


class Hall(Room):
    def center(self):
        print_pause("You're in the hall!")
        print_pause("In front of you there's the main door of the house.")
        print_pause("On your right there's a door.")
        print_pause("Backwards there's the hallway.")
        print_pause("On your left there's another door.")

        self.move()

    """ BACKWARD """

    def backward(self):
        self.thehouse.rooms["hallway"].center()

    """ LEFT """

    def left(self):
        print_pause("You open the door and enter the room")
        self.thehouse.rooms["kitchen"].center()
