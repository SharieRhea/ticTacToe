import random
from moves import Moves


def get_random_move(info):
    number = random.randint(0, 8)
    while info[number].get_move() is not Moves.NONE:
        number = random.randint(0, 8)
    return number


class RandomComputer:
    """Models a computer players that picks random moves."""

    def __init__(self):
        self.symbol = True

    def get_computer_move(self, info):
        return get_random_move(info)


class HumanComputer:
    """Models a 'human-like' computer player."""

    def __init__(self):
        self.symbol = True

    def get_computer_move(self, info):
        """Returns a move to win, block the other player, or randomly, in that order."""
        possibility_count = 0
        block_move = None
        for possibility in self.get_possibilities(info):
            # create set of unique moves in line
            moves = set()
            for move in possibility:
                moves.add(move)

            # check for opportunity
            if len(moves) == 2 and possibility.count(Moves.NONE) == 1:
                move_index = possibility.index(Moves.NONE)
                # find exact tile number
                if Moves.COMPUTER in moves:
                    return self.get_tile_index(possibility_count, move_index)
                elif Moves.PLAYER in moves:
                    block_move = self.get_tile_index(possibility_count, move_index)

            possibility_count += 1

        if block_move is not None:
            return block_move
        return get_random_move(info)

    def get_possibilities(self, tiles):
        """Returns the 8 possible lines to win a tic-tac-toe game"""
        return [
            [tiles[0].get_move(), tiles[1].get_move(), tiles[2].get_move()],
            [tiles[3].get_move(), tiles[4].get_move(), tiles[5].get_move()],
            [tiles[6].get_move(), tiles[7].get_move(), tiles[8].get_move()],
            [tiles[0].get_move(), tiles[3].get_move(), tiles[6].get_move()],
            [tiles[1].get_move(), tiles[4].get_move(), tiles[7].get_move()],
            [tiles[2].get_move(), tiles[5].get_move(), tiles[8].get_move()],
            [tiles[0].get_move(), tiles[4].get_move(), tiles[8].get_move()],
            [tiles[2].get_move(), tiles[4].get_move(), tiles[6].get_move()]]

    def get_tile_index(self, line, index):
        """Returns the index of tile (0-8) based on its line and position."""
        # horizontal lines
        if line < 3:
            return line * 3 + index
        # vertical lines
        elif line < 6:
            return index * 3 + line % 3
        # diagonal lines
        elif line == 6:
            if index == 0:
                return 0
            elif index == 1:
                return 4
            else:
                return 8
        else:
            if index == 0:
                return 2
            elif index == 1:
                return 4
            else:
                return 6
