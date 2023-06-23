import pygame

from moves import Moves
from spritesheet import SpriteSheet
from tempboard import TempTile


class Tile:
    """Models an individual tile on the board."""

    def __init__(self, x_pos, y_pos, width):
        """Initializes a tile."""
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width

        # Rect used for mouse collision
        self.rect = pygame.Rect((x_pos, y_pos), (width, width))

        self.x = SpriteSheet("sprites/X.png", 2, 16, 16, 4, (0, 0, 0))
        self.o = SpriteSheet("sprites/O.png", 2, 16, 16, 4, (0, 0, 0))
        self.move = Moves.NONE

        # Loads highlight sprite for the tile
        highlight = pygame.image.load("sprites/highlightedTile.png").convert_alpha()
        highlight.set_colorkey((0, 0, 0))
        self.highlight = pygame.transform.scale(highlight, (width, width))

    def draw(self, screen, frame):
        """Draws the respective move for that tile."""
        if self.move is Moves.PLAYER:
            self.x.play_animation(screen, frame, (self.x_pos, self.y_pos))
        elif self.move is Moves.COMPUTER:
            self.o.play_animation(screen, frame, (self.x_pos, self.y_pos))
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.highlight, (self.x_pos, self.y_pos))

    def check_clicked(self):
        """Checks if the tile is currently being clicked."""
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

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
