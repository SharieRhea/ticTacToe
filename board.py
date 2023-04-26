import pygame
import tile


class Board:
    """Models a TicTacToe board in its current state."""

    def __init__(self):
        """Initializes an empty board object."""
        self.board = pygame.image.load("sprites/board.png").convert_alpha()
        self.board.set_colorkey((0, 0, 0))
        self.board = pygame.transform.scale(self.board, (192, 192))

        self.positions = [(154, 154), (218, 154), (282, 154), (154, 218), (218, 218), (282, 218), (154, 282),
                          (218, 282), (282, 282)]
        self.tiles = [tile.Tile(154, 154, 64, 64), tile.Tile(218, 154, 64, 64), tile.Tile(282, 154, 64, 64),
                      tile.Tile(154, 218, 64, 64), tile.Tile(218, 218, 64, 64), tile.Tile(282, 218, 64, 64),
                      tile.Tile(154, 282, 64, 64), tile.Tile(218, 282, 64, 64), tile.Tile(282, 282, 64, 64)]

    def draw_board(self, screen):
        """Draws the board in its current state."""
        screen.blit(self.board, (154, 154))
        for box in self.tiles:
            box.draw_move(screen)
            box.draw_highlighted(screen)
            box.add_move()
