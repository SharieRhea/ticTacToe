import random

import pygame


def get_computer_move(moves):
    number = random.randint(0, 8)
    while moves[number].get_move() is not None:
        number = random.randint(0, 8)
    return number


class RandomComputer:
    """Models a computer playing that simply picks a random move on its turn."""

    def __init__(self):
        self.symbol = True
