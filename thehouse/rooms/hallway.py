from helpers import print_pause

from .room import Room


class Hallway(Room):
    def center(self):
        print_pause("You are in the hallway.")
        print_pause("Behind you there's a door.")
        print_pause("On your left there's a door and two paintings.")
        print_pause("On your right there's a little table and a door.")
        print_pause("In front of you there's the hall of the house.")
        print_pause("Where do you want to go?")
