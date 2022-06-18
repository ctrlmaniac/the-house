from helpers import print_pause, validate_input

from .room import Room
from characters import Monster


class Livingroom(Room):
    def __init__(self, player, thehouse):
        super().__init__(player, thehouse)
        self.monster = Monster(self.player)

    def center(self):
        print_pause("You're in the livingroom!")

        if self.monster.is_alive():
            print_pause("There's a terrible monster!")
            print_pause("It's half human and half something undescribable!")
            print_pause(
                "Luckly it's slow, but one of its sort of tentacle tries to grab you!"
            )
            print_pause("Do you want to fight or escape?")

            choice = validate_input("Type fight or escape: ", ["fight", "escape"])

            if choice == "fight":
                self.fight()
            else:
                self.escape()

    def fight(self):
        while self.monster.is_alive():
            damage = 1
            print_pause("It's your turn to deal damages!")
            print_pause(f"You deal {damage} damage.")
            self.monster.loose_health()

            print_pause("It's the monster's turn to deal damages!")
            self.monster.deals_damage()

            if not self.player.is_alive():
                break
            else:
                choice = validate_input("Type fight or escape: ", ["fight", "escape"])

                if choice == "fight":
                    self.fight()
                    break
                else:
                    self.escape()
                    break

    def escape(self):
        pass
