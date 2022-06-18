from helpers import print_pause, validate_input
from .room import Room


class Bedroom(Room):
    def center(self):
        print_pause("You're in the bedroom!")
        print_pause("On your right there's a window.")
        print_pause("On your left there's a door")
        print_pause("Backwards there's a bed.")
        print_pause("In front of you there's a dresser.")

        self.move()

    """ LEFT """

    def left(self):
        self.thehouse.rooms["hallway"].center()

    """ BACKWARD """

    def backward(self):
        print_pause("You look tired.")
        print_pause("Do you want to rest a little bit?")

        choice = validate_input("Type yes or no: ", ["yes", "no"])

        if choice == "yes":
            print_pause("You've decided to rest.", 2)
            print_pause(".", 2)
            print_pause(".", 2)
            print_pause(".", 2)
            self.player.restore_health()
        else:
            print_pause("You go back.")

        self.move()

    """ RIGHT """

    def right(self):
        print_pause("You look outside of the window.")
        print_pause("Outside it's pitch black!")
        print_pause("There's something that moves in the darkness")
        print_pause("It's moving so fast that you barely can see it...")
        print_pause("You wonder how could you escape this house")
        print_pause("And if it's safe outside either...", 3)
        print_pause("You go back.")

        self.move()
