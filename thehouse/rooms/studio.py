import random

from helpers import print_pause, validate_input


class Studio:
    def __init__(self, player):
        self.player = player
        self.lights = random.choice([True, False])

    def intro(self):
        lights = "on" if self.lights else "off"
        switch_position = random.choice(["right", "left", "forward", "backward"])
        guesses = 0
        chances = random.randint(2, 3)

        print_pause("You open your eyes and find yourself lying on the floor")
        print_pause("Your head is pounding and it hurts")
        print_pause("With a lot of effort you stand up")
        print_pause(f"You find yourself in a room with the lights {lights}")

        if not self.lights:
            print_pause("You hear something lurking in the dark")
            print_pause("You defenetly want to turn the lights on.")
            print_pause("You extend your arms to:")
            print_pause("- the right")
            print_pause("- the left")
            print_pause("- forward")
            print_pause("- backward")

            while True:
                choice = validate_input(
                    "Type right, left, forward or backward: ",
                    ["right", "left", "backward", "forward"],
                )

                if choice == switch_position:
                    print_pause("You've turned the lights on!")
                    break
                else:
                    guesses += 1
                    print_pause("There's nothing here!")
                    print_pause(
                        "But you sense there's something "
                        "that want to reach your hand..."
                    )

                    if guesses >= chances:
                        print_pause("Random death")
                        print_pause("game over!")
                        exit()
