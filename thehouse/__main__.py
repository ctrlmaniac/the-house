"""This main module will run the game.

Type python -m thehouse and the game will run.
"""

from thehouse.thehouse import TheHouse
from thehouse.characters import Player

player = Player()
game = TheHouse(player)

game.play()
