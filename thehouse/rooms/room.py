from helpers import validate_input


class Room:
    def right(self):
        pass

    def left(self):
        pass

    def backward(self):
        pass

    def forward(self):
        pass

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
