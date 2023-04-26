import pygame


class Board:
    """Models a TicTacToe board in its current state."""

    def __init__(self, x, o):
        """Initializes an empty board object."""
        self.board = pygame.image.load("sprites/board.png").convert_alpha()
        self.board.set_colorkey((0, 0, 0))
        self.board = pygame.transform.scale(self.board, (192, 192))
        self.moves = [[1, None, None], [None, None, None], [None, None, None]]
        self.x = x
        self.o = o

        self.positions = [(154, 154), (218, 154), (282, 154), (154, 218), (218, 218), (282, 218), (154, 282),
                          (218, 282), (282, 282)]
        self.tiles = [pygame.Rect(self.positions[0], (64, 64)), pygame.Rect(self.positions[1], (64, 64)),
                      pygame.Rect(self.positions[2], (64, 64)), pygame.Rect(self.positions[3], (64, 64)),
                      pygame.Rect(self.positions[4], (64, 64)), pygame.Rect(self.positions[5], (64, 64)),
                      pygame.Rect(self.positions[6], (64, 64)), pygame.Rect(self.positions[7], (64, 64)),
                      pygame.Rect(self.positions[8], (64, 64))]

    def draw_board(self, screen):
        """Draws the board in its current state."""
        screen.blit(self.board, (154, 154))
        self.check_hover(screen)
        count = 0
        for row in self.moves:
            for move in row:
                if move == 0:
                    self.x.play_animation(screen, self.positions[count])
                elif move == 1:
                    self.o.play_animation(screen, self.positions[count])
                count += 1

    def check_hover(self, screen):
        for tile in self.tiles:
            if tile.collidepoint(pygame.mouse.get_pos()):
                highlight = pygame.image.load("sprites/highlightedTile.png").convert_alpha()
                highlight.set_colorkey((0, 0, 0))
                highlight = pygame.transform.scale(highlight, (64, 64))
                screen.blit(highlight, (tile.x, tile.y))
