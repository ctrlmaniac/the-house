from helpers import validate_input, print_pause


class Game:
    def play_game(self):
        choice = validate_input("Choose (1) One or (2) Two: ", ["1", "2"])

        print_pause(choice)
