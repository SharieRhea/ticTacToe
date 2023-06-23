from moves import Moves


class TempTile:
    """Models an individual tile on the board with no graphics, only move data."""

    def __init__(self):
        """Initializes a tile."""
        self.move = Moves.NONE

    def add_player_move(self):
        """Alters the current state of the tile to reflect a player move."""
        self.move = Moves.PLAYER

    def add_computer_move(self):
        """Alters the current state of the tile to reflect a computer move."""
        self.move = Moves.COMPUTER

    def get_move(self):
        """Returns the tile's current move/status."""
        return self.move

    def copy(self):
        tile = TempTile()
        tile.move = self.get_move()
        return tile


class TempBoard:
    """Models a TicTacToe board in its current state with no graphics, only move data."""

    def __init__(self, computer):
        """Initializes an empty board object."""
        self.computer = computer
        self.player_turn = True

        self.tiles = [TempTile(), TempTile(), TempTile(), TempTile(), TempTile(), TempTile(), TempTile(), TempTile(),
                      TempTile()]

    def is_board_full(self):
        """Checks if the board is full."""
        for move in self.tiles:
            if move.get_move() is Moves.NONE:
                return False
        return True

    def get_possibilities(self):
        """Returns a move to win, block the other player, or randomly, in that order."""
        return [
            [self.tiles[0], self.tiles[1], self.tiles[2]],
            [self.tiles[3], self.tiles[4], self.tiles[5]],
            [self.tiles[6], self.tiles[7], self.tiles[8]],
            [self.tiles[0], self.tiles[3], self.tiles[6]],
            [self.tiles[1], self.tiles[4], self.tiles[7]],
            [self.tiles[2], self.tiles[5], self.tiles[8]],
            [self.tiles[0], self.tiles[4], self.tiles[8]],
            [self.tiles[2], self.tiles[4], self.tiles[6]]]

    def check_win(self):
        """Checks the board for a win from either side, returns Moves.NONE if there is no win."""
        for possibility in self.get_possibilities():
            moves = set()
            for tile in possibility:
                moves.add(tile.get_move())
            if len(moves) == 1 and not moves.__contains__(Moves.NONE):
                for move in moves:
                    return move
        return Moves.NONE

    def get_tiles(self):
        return self.tiles

    def copy(self):
        board = TempBoard(self.computer)
        board.tiles = [tile.copy() for tile in self.get_tiles()]
        board.player_turn = self.player_turn
        return board
