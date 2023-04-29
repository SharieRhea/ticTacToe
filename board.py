import pygame
import tile
import randomcomputer


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
        self.computer = randomcomputer.RandomComputer
        self.player_turn = True

    def draw_board(self, screen):
        """Draws the board in its current state."""
        screen.blit(self.board, (154, 154))
        count = 0
        for box in self.tiles:
            box.draw_move(screen)
            if box.rect.collidepoint(pygame.mouse.get_pos()):
                box.draw_highlighted(screen)
            if self.player_turn:
                if box.rect.collidepoint(pygame.mouse.get_pos()):
                    if box.add_player_move():
                        self.player_turn = False
        if not self.player_turn:
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
        self.tiles[randomcomputer.get_move(self.tiles)].add_computer_move()
