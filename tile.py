import pygame


class Tile:
    """Models an individual tile on the board."""

    def __init__(self, move, x_pos, y_pos, width, height):
        """Initializes a tile."""
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.width = width
        self.height = height

        # Rect used for mouse collision
        self.rect = pygame.Rect((x_pos, y_pos), (width, height))

        self.move = move

        # Loads highlight sprite for the tile
        highlight = pygame.image.load("sprites/highlightedTile.png").convert_alpha()
        highlight.set_colorkey((0, 0, 0))
        self.highlight = pygame.transform.scale(highlight, (width, height))

    def draw_highlighted(self, screen):
        """Draws a highlighted tile if it is being hovered and does not have a move."""
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.move is None:
            screen.blit(self.highlight, (self.x_pos, self.y_pos))

    def draw_move(self, screen):
        """Draws the respective move for that tile."""
        if self.move is not None:
            self.move.play_animation(screen, (self.x_pos, self.y_pos))
