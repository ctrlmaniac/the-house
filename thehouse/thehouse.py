import rooms

from helpers import print_pause, validate_input


class TheHouse:
    def __init__(self, player):
        self.player = player
        self.rooms = {
            "studio": rooms.Studio(self.player),
        }

    def play_again(self):
        print_pause("Do you want to play again the game?")

        choice = validate_input("Type yes or no: ", ["yes", "no"])

        if choice == "yes":
            # bug: doesn't work properly
            self.play_game()
        else:
            quit()

    def play_game(self):
        while self.player.is_alive():
            self.rooms["studio"].intro()
        else:
            print("You died!")

        self.play_again()
