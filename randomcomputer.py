import random
from moves import Moves


class RandomComputer:
    """Models a computer players that picks random moves."""
    def __init__(self):
        self.symbol = True

    def get_computer_move(self, info):
        number = random.randint(0, 8)
        while info[number].get_move() is not Moves.NONE:
            number = random.randint(0, 8)
        return number
