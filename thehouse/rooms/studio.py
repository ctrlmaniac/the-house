import random

from helpers import print_pause, validate_input


class Studio:
    def __init__(self, player):
        self.player = player
        self.lights = random.choice([True, False])

    def prompt_light(self):
        switch_position = random.choice(["right", "left", "forward", "backward"])

        print_pause("You hear something lurking in the dark")
        print_pause("You defenetly want to turn the lights on.")
        print_pause("You extend your arms to:")
        print_pause("- the right")
        print_pause("- the left")
        print_pause("- forward")
        print_pause("- backward")

        while self.player.health > 0:
            choice = validate_input(
                "Type right, left, forward or backward: ",
                ["right", "left", "backward", "forward"],
            )

            if choice == switch_position:
                print_pause("You've turned the lights on!")
                break
            else:
                print_pause("There's nothing here!")
                print_pause(
                    "But you sense there's something " "that want to reach your hand..."
                )
                self.player.loose_health()

    def intro(self):
        lights = "on" if self.lights else "off"

        print_pause("You open your eyes and find yourself lying on the floor")
        print_pause("Your head is pounding and it hurts")
        print_pause("With a lot of effort you stand up")
        print_pause(f"You find yourself in a room with the lights {lights}")

        if not self.lights:
            self.prompt_light()

        if self.player.is_alive():
            self.center()

    def move(self):
        choice = validate_input(
            'Type "right", "left", "forward" or "backward": ',
            ["right", "left", "forward", "backward"],
        )

        if choice == "right":
            self.right()
        elif choice == "left":
            self.left()
        elif choice == "backward":
            self.backward()
        elif choice == "forward":
            self.forward()

    def center(self):
        print_pause("You're in the middle of a studio")
        print_pause("Behind you there's a desk with some papers on it.")
        print_pause("On your left there's a shelf with many books on it.")
        print_pause("On your right there's a window.")
        print_pause("In front of you there's a closed door.")
        print_pause("What are you gonna do?")

        self.move()

    def right(self):
        print("the right")

    def left(self):
        print("left")

    def backward(self):
        print("back")

    def forward(self):
        print("forward")
