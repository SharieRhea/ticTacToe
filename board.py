import pygame


class Board:
    """Models a TicTacToe board in its current state."""

    def __init__(self, x, o):
        """Initializes an empty board object."""
        self.board = pygame.image.load("sprites/board.png").convert_alpha()
        self.board.set_colorkey((0, 0, 0))
        self.board = pygame.transform.scale(self.board, (192, 192))
        self.moves = [[None, None, None], [None, None, None], [None, None, None]]
        self.x = x
        self.o = o

        self.position = [(154, 154), (218, 154), (282, 154), (154, 218), (218, 218), (282, 218), (154, 282), (218, 282),
                         (282, 282)]

    def draw_board(self, screen):
        """Draws the board in its current state."""
        screen.blit(self.board, (154, 154))
        count = 0
        for row in self.moves:
            for move in row:
                if move == 0:
                    self.x.play_animation(screen, self.position[count])
                elif move == 1:
                    self.o.play_animation(screen, self.position[count])
                count += 1
