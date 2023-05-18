import pygame

from moves import Moves
from tile import Tile


class Board:
    """Models a TicTacToe board in its current state."""

    def __init__(self, location, computer):
        """Initializes an empty board object."""
        self.board = pygame.image.load("sprites/board.png").convert_alpha()
        self.board.set_colorkey((0, 0, 0))
        self.board = pygame.transform.scale(self.board, (192, 192))
        self.location = location
        self.computer = computer
        self.player_turn = True

        tile_size = 64
        self.positions = [(location[0], location[1]), (location[0] + tile_size, location[1]),
                          (location[0] + 2 * tile_size, location[1]), (location[0], location[1] + tile_size),
                          (location[0] + tile_size, location[1] + tile_size),
                          (location[0] + 2 * tile_size, location[1] + tile_size),
                          (location[0], location[1] + 2 * tile_size),
                          (location[0] + tile_size, location[1] + 2 * tile_size),
                          (location[0] + 2 * tile_size, location[1] + 2 * tile_size)]
        self.tiles = [Tile(self.positions[0][0], self.positions[0][1], tile_size),
                      Tile(self.positions[1][0], self.positions[1][1], tile_size),
                      Tile(self.positions[2][0], self.positions[2][1], tile_size),
                      Tile(self.positions[3][0], self.positions[3][1], tile_size),
                      Tile(self.positions[4][0], self.positions[4][1], tile_size),
                      Tile(self.positions[5][0], self.positions[5][1], tile_size),
                      Tile(self.positions[6][0], self.positions[6][1], tile_size),
                      Tile(self.positions[7][0], self.positions[7][1], tile_size),
                      Tile(self.positions[8][0], self.positions[8][1], tile_size)]

    def draw_board(self, screen):
        """Draws the board in its current state and runs a turn."""
        screen.blit(self.board, (self.location[0], self.location[1]))
        for box in self.tiles:
            box.draw(screen)
        self.run_turn()

    def display_board(self, screen):
        """Displays the board in its current state."""
        screen.blit(self.board, (self.location[0], self.location[1]))
        for box in self.tiles:
            box.draw(screen)

    def is_board_full(self):
        """Checks if the board is full."""
        for move in self.tiles:
            if move.get_move() is Moves.NONE:
                return False
        return True

    def get_possibilities(self):
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
        for possibility in self.get_possibilities():
            moves = set()
            for tile in possibility:
                moves.add(tile.get_move())
            if len(moves) == 1:
                for move in moves:
                    return move
        return Moves.NONE

    def computer_turn(self):
        self.tiles[self.computer.get_computer_move(self.tiles)].add_computer_move()

    def run_turn(self):
        if self.player_turn and not self.is_board_full():
            for box in self.tiles:
                if box.check_clicked():
                    if box.get_move() is Moves.NONE:
                        box.add_player_move()
                        self.player_turn = False
        elif not self.player_turn and not self.is_board_full():
            self.computer_turn()
            self.player_turn = True
            pygame.time.wait(250)
