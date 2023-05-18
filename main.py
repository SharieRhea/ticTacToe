import pygame

from moves import Moves
from spritesheet import SpriteSheet
from button import Button
from board import Board
from randomcomputer import RandomComputer
from humancomputer import HumanComputer

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((512, 512))
BG = (50, 50, 50)
alpha = (0, 0, 0)

# initialize graphics
background = pygame.image.load("sprites/background.png")
title = SpriteSheet("sprites/ticTacToe.png", 7, 96, 48, 4, alpha)

# initialize buttons
play_regular = SpriteSheet("sprites/play.png", 1, 48, 32, 4, alpha)
play_highlighted = SpriteSheet("sprites/playHighlighted.png", 2, 48, 32, 4, alpha)
play = Button(screen, play_regular, play_highlighted)
quit_regular = SpriteSheet("sprites/quit.png", 1, 48, 32, 4, alpha)
quit_highlighted = SpriteSheet("sprites/quitHighlighted.png", 2, 48, 32, 4, alpha)
quit_button = Button(screen, quit_regular, quit_highlighted)
random_regular = SpriteSheet("sprites/random.png", 1, 64, 32, 4, alpha)
random_highlighted = SpriteSheet("sprites/randomHighlighted.png", 2, 64, 32, 4, alpha)
random_button = Button(screen, random_regular, random_highlighted)
human_regular = SpriteSheet("sprites/human.png", 1, 64, 32, 4, alpha)
human_highlighted = SpriteSheet("sprites/humanHighlighted.png", 2, 64, 32, 4, alpha)
human_button = Button(screen, human_regular, human_highlighted)
insane_regular = SpriteSheet("sprites/insane.png", 1, 64, 32, 4, alpha)
insane_highlighted = SpriteSheet("sprites/insaneHighlighted.png", 2, 64, 32, 4, alpha)
insane_button = Button(screen, insane_regular, insane_highlighted)

# initialize win/loss screens
win = SpriteSheet("sprites/win.png", 2, 96, 48, 4, (0, 0, 0))
draw = SpriteSheet("sprites/draw.png", 2, 96, 48, 4, (0, 0, 0))
lose = SpriteSheet("sprites/loss.png", 2, 96, 48, 4, (0, 0, 0))

# state variables
playing = False
first_game = True
selection = False

while True:
    screen.blit(background, (0, 0))

    # displays title screen
    if first_game:
        title.play_animation(screen, (66, 66))
        play.draw((48, 186))
        quit_button.draw((272, 186))
        if play.check_clicked():
            selection = True
            first_game = False
            # Delay prevents multiple clicks from registering
            pygame.time.delay(250)
        if quit_button.check_clicked():
            pygame.quit()
            raise SystemExit
    # displays computer player selection screen
    elif selection:
        random_button.draw((128, 48))
        human_button.draw((128, 192))
        insane_button.draw((128, 336))
        if random_button.check_clicked():
            playing = True
            selection = False
            gameboard = Board((160, 160), RandomComputer())
        if human_button.check_clicked():
            playing = True
            selection = False
            gameboard = Board((160, 160), HumanComputer())
    # game must be over, display win/loss screen, play/quit options, and completed board
    elif not playing:
        gameboard.display_board(screen)
        if gameboard.check_win() is Moves.PLAYER:
            win.play_animation(screen, (66, 12))
        elif gameboard.check_win() is Moves.COMPUTER:
            lose.play_animation(screen, (66, 12))
        elif gameboard.is_board_full():
            draw.play_animation(screen, (66, 12))
        play.draw((48, 372))
        quit_button.draw((272, 372))
        if play.check_clicked():
            selection = True
            # Delay prevents multiple clicks from registering
            pygame.time.delay(250)
        if quit_button.check_clicked():
            pygame.quit()
            raise SystemExit
    # active game
    else:
        gameboard.draw_board(screen)
        if gameboard.check_win() is not Moves.NONE or gameboard.is_board_full():
            playing = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()
    clock.tick(30)
