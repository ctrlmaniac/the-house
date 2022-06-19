from .room import Room

from helpers import print_pause


class Diningroom(Room):
    def center(self):
        print_pause("You're in the dining room!")
        print_pause("There's a bloody mess here...")
        print_pause("Someone or something has killed three poeple!")
        print_pause("Forward there's a corpse!")
        print_pause("On your left there's another corpse!")
        print_pause("On your back there's a third corpse!")
        print_pause("On your left there's a door.")
        print_pause("Maybe you can check the pockets of the corpse!")

        self.move()
