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

    """ BACKWARD """

    def backward(self):
        print_pause("You look tired.")
        print_pause("Do you want to rest a little bit?")

        choice = validate_input("Type yes or no: ", ["yes", "no"])

        if choice == "yes":
            print_pause("You've decided to rest.", 5)
            self.player.restore_health()
        else:
            print_pause("You go back.")

        self.move()
