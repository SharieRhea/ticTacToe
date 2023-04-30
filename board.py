import pygame

import spritesheet
import tile
import randomcomputer


class Board:
    """Models a TicTacToe board in its current state."""

    def __init__(self, location):
        """Initializes an empty board object."""
        self.board = pygame.image.load("sprites/board.png").convert_alpha()
        self.board.set_colorkey((0, 0, 0))
        self.board = pygame.transform.scale(self.board, (192, 192))
        self.location = location
        self.player_turn = True

        tile_size = 64
        self.positions = [(location[0], location[1]), (location[0]+tile_size, location[1]),
                          (location[0]+2*tile_size, location[1]), (location[0], location[1]+tile_size),
                          (location[0]+tile_size, location[1]+tile_size), (location[0]+2*tile_size, location[1]+tile_size),
                          (location[0], location[1]+2*tile_size), (location[0]+tile_size, location[1]+2*tile_size),
                          (location[0]+2*tile_size, location[1]+2*tile_size)]
        self.tiles = [tile.Tile(self.positions[0][0], self.positions[0][1], tile_size), tile.Tile(self.positions[1][0], self.positions[1][1], tile_size), tile.Tile(self.positions[2][0], self.positions[2][1], tile_size),
                      tile.Tile(self.positions[3][0], self.positions[3][1], tile_size), tile.Tile(self.positions[4][0], self.positions[4][1], tile_size), tile.Tile(self.positions[5][0], self.positions[5][1], tile_size),
                      tile.Tile(self.positions[6][0], self.positions[6][1], tile_size), tile.Tile(self.positions[7][0], self.positions[7][1], tile_size), tile.Tile(self.positions[8][0], self.positions[8][1], tile_size)]

    def draw_board(self, screen):
        """Draws the board in its current state."""
        screen.blit(self.board, (self.location[0], self.location[1]))
        for box in self.tiles:
            box.draw(screen)
        self.run_turn(screen)

    def is_board_full(self):
        """Checks if the board is full."""
        for move in self.tiles:
            if move.get_move() is None:
                return False
        return True

    def check_win(self):
        return False

    def computer_turn(self):
        self.tiles[randomcomputer.get_computer_move(self.tiles)].set_move(False)

    def run_turn(self, screen):
        if self.player_turn and not self.is_board_full():
            for box in self.tiles:
                if self.player_turn:
                    if box.check_clicked():
                        box.set_move(True)
                        self.player_turn = False
        elif not self.player_turn and not self.is_board_full():
            self.computer_turn()
            self.player_turn = True
            pygame.time.wait(250)
