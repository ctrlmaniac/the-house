from thehouse import TheHouse
from characters import Player
from helpers import validate_input, print_pause


def play():
    player = Player()
    thehouse = TheHouse(player)

    thehouse.play_game()

    print_pause("Do you want to play again?")
    choice = validate_input("Type yes or no: ", ["yes", "no"])

    if choice == "yes":
        play()
    else:
        quit()


play()
