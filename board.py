import pygame
import tile


class Board:
    """Models a TicTacToe board in its current state."""

    def __init__(self, x, o):
        """Initializes an empty board object."""
        self.board = pygame.image.load("sprites/board.png").convert_alpha()
        self.board.set_colorkey((0, 0, 0))
        self.board = pygame.transform.scale(self.board, (192, 192))
        self.x = x
        self.o = o

        self.positions = [(154, 154), (218, 154), (282, 154), (154, 218), (218, 218), (282, 218), (154, 282),
                          (218, 282), (282, 282)]
        self.tiles = [tile.Tile(self.x, 154, 154, 64, 64), tile.Tile(None, 218, 154, 64, 64), tile.Tile(None, 282, 154, 64, 64),
                      tile.Tile(None, 154, 218, 64, 64), tile.Tile(self.o, 218, 218, 64, 64), tile.Tile(None, 282, 218, 64, 64),
                      tile.Tile(None, 154, 282, 64, 64), tile.Tile(None, 218, 282, 64, 64), tile.Tile(None, 282, 282, 64, 64)]

    def draw_board(self, screen):
        """Draws the board in its current state."""
        screen.blit(self.board, (154, 154))
        for box in self.tiles:
            box.draw_move(screen)
            box.draw_highlighted(screen)
