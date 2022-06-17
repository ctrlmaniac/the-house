import random
from ..helpers import print_pause


class Studio:
    def __init__(self):
        self.lights = random.choice([True, False])

    def intro(self):
        lights = "on" if self.lights else "off"

        print_pause("You open your eyes and find yourself lying on the floor")
        print_pause("Your head is pounding and it hurts")
        print_pause("With a lot of effort you stand up")
        print_pause(f"You find yourself in a room with the lights {lights}")
