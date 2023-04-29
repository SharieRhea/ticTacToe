import pygame
import tile
import randomcomputer


class Board:
    """Models a TicTacToe board in its current state."""

    def __init__(self, location):
        """Initializes an empty board object."""
        self.board = pygame.image.load("sprites/board.png").convert_alpha()
        self.board.set_colorkey((0, 0, 0))
        self.board = pygame.transform.scale(self.board, (192, 192))
        tile_size = 64
        self.positions = [(location[0], location[1]), (location[0]+tile_size, location[1]),
                          (location[0]+2*tile_size, location[1]), (location[0], location[1]+tile_size),
                          (location[0]+tile_size, location[1]+tile_size), (282, location[1]+tile_size),
                          (location[0], 282), (location[0]+tile_size, location[1]+2*tile_size),
                          (location[0]+2*tile_size, location[1]+2*tile_size)]
        self.tiles = [tile.Tile(154, 154, 64), tile.Tile(218, 154, 64), tile.Tile(282, 154, 64),
                      tile.Tile(154, 218, 64), tile.Tile(218, 218, 64), tile.Tile(282, 218, 64),
                      tile.Tile(154, 282, 64), tile.Tile(218, 282, 64), tile.Tile(282, 282, 64)]
        self.player_turn = True

    def draw_board(self, screen):
        """Draws the board in its current state."""
        screen.blit(self.board, (154, 154))
        for box in self.tiles:
            box.draw(screen)
            if self.player_turn:
                if box.check_clicked():
                    box.set_move(True)
                    self.player_turn = False
        if not self.player_turn and not self.is_board_full():
            self.computer_turn()
            self.player_turn = True
            pygame.time.wait(250)

    def is_board_full(self):
        """Checks if the board is full."""
        for move in self.tiles:
            if move.get_move() is None:
                return False
        return True

    def computer_turn(self):
        self.tiles[randomcomputer.get_computer_move(self.tiles)].set_move(False)
