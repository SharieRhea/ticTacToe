import random

from moves import Moves


class HumanComputer:
    """Models a 'human-like" computer player."""

    def __init__(self):
        self.symbol = True

    def get_computer_move(self, info):
        possibility_count = 0
        for possibility in self.get_possibilities(info):
            # create set of unique moves in line
            moves = set()
            for move in possibility:
                moves.add(move)

            # check for opportunity
            if len(moves) == 2 and Moves.NONE in moves:
                empties = 0
                for move in possibility:
                    if move is Moves.NONE:
                        empties += 1

                if empties == 1:
                    move_index = possibility.index(Moves.NONE)

                    # find exact tile number
                    return self.get_tile_index(possibility_count, move_index)
            possibility_count += 1

        return self.get_random_move(info)

    def get_possibilities(self, tiles):
        return [
            [tiles[0].get_move(), tiles[1].get_move(), tiles[2].get_move()],
            [tiles[3].get_move(), tiles[4].get_move(), tiles[5].get_move()],
            [tiles[6].get_move(), tiles[7].get_move(), tiles[8].get_move()],
            [tiles[0].get_move(), tiles[3].get_move(), tiles[6].get_move()],
            [tiles[1].get_move(), tiles[4].get_move(), tiles[7].get_move()],
            [tiles[2].get_move(), tiles[5].get_move(), tiles[8].get_move()],
            [tiles[0].get_move(), tiles[4].get_move(), tiles[8].get_move()],
            [tiles[2].get_move(), tiles[4].get_move(), tiles[6].get_move()]]

    def get_random_move(self, info):
        number = random.randint(0, 8)
        while info[number].get_move() is not Moves.NONE:
            number = random.randint(0, 8)
        return number

    def get_tile_index(self, line, index):
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
