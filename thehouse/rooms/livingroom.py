import random

from characters import Monster
from helpers import print_pause, validate_input

from .room import Room


class Livingroom(Room):
    def __init__(self, player, thehouse):
        super().__init__(player, thehouse)
        self.monster = Monster(self.player)
        self.tries = random.randint(3, 6)

    def center(self):
        print_pause("You're in the livingroom!")

        if self.monster.is_alive():
            print_pause("There's a terrible monster!")
            print_pause("It's half human and half something undescribable!")
            print_pause(
                "Luckly it's slow, but one of its sort of tentacle tries to grab you!"
            )
            self.fight_or_escape()
        else:
            # add feature
            print_pause("something to add")

            self.move()

    def fight_or_escape(self):
        print_pause("Do you want to fight or escape?")
        choice = validate_input("Type fight or escape: ", ["fight", "escape"])

        if choice == "fight":
            self.fight()
        else:
            self.escape()

    def fight(self):
        while self.monster.is_alive():
            print_pause("It's your turn to deal damages!")

            if "knife" not in self.player.items:
                damage = 1
                print_pause("It seems like you need something to deal more damages!")
            else:
                damage = random.randint(2, 4)

            print_pause(f"You deal {damage} damage.")
            self.monster.loose_health(damage)

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
        print_pause("You're trying to escape the monster!")

        choice = validate_input(
            "Type a number between 1 and 6 included: ", ["1", "2", "3", "4", "5", "6"]
        )

        if int(choice) == random.randint(1, 6):
            print_pause("You successfully escaped the moster!!")
            self.thehouse.rooms["hallway"].center()
        else:
            print_pause("You panic and can't escape the fight!")
            self.tries -= 1

            if self.tries <= 0:
                print_pause("The monster reached you!")
                self.monster.deals_damage()
                self.tries = random.randint(3, 6)

            self.fight_or_escape()
