import pygame

import moves
import spritesheet


class Tile:
    """Models an individual tile on the board."""

    def __init__(self, x_pos, y_pos, width):
        """Initializes a tile."""
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width

        # Rect used for mouse collision
        self.rect = pygame.Rect((x_pos, y_pos), (width, width))

        self.x = spritesheet.SpriteSheet("sprites/X.png", 2, 16, 16, 4, (0, 0, 0))
        self.o = spritesheet.SpriteSheet("sprites/O.png", 2, 16, 16, 4, (0, 0, 0))
        self.move = moves.Moves.NONE

        # Loads highlight sprite for the tile
        highlight = pygame.image.load("sprites/highlightedTile.png").convert_alpha()
        highlight.set_colorkey((0, 0, 0))
        self.highlight = pygame.transform.scale(highlight, (width, width))

    def draw(self, screen):
        """Draws the respective move for that tile."""
        if self.move is moves.Moves.PLAYER:
            self.x.play_animation(screen, (self.x_pos, self.y_pos))
        elif self.move is moves.Moves.COMPUTER:
            self.o.play_animation(screen, (self.x_pos, self.y_pos))
        elif self.rect.collidepoint(pygame.mouse.get_pos()):
            screen.blit(self.highlight, (self.x_pos, self.y_pos))

    def check_clicked(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True

    def add_player_move(self):
        """Alters the current state of the tile to reflect its move."""
        self.move = moves.Moves.PLAYER

    def add_computer_move(self):
        """Alters the current state of the tile to reflect a computer move."""
        self.move = moves.Moves.COMPUTER

    def get_move(self):
        return self.move
