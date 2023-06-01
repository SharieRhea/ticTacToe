import pygame

from states import States
from moves import Moves
from spritesheet import SpriteSheet
from button import Button
from board import Board
import computers
from timer import Timer

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
play_button = Button(screen, play_regular, play_highlighted)
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
tie = SpriteSheet("sprites/draw.png", 2, 96, 48, 4, (0, 0, 0))
lose = SpriteSheet("sprites/loss.png", 2, 96, 48, 4, (0, 0, 0))

state = States.TITLE
timer = Timer("sprites/numbers.png")


def play_button_clicked():
    """Updates state to reflect game status."""
    if play_button.check_clicked():
        global state
        state = States.SELECTION
        # Delay prevents multiple clicks from registering
        pygame.time.delay(250)


def selection_clicked():
    global state
    state = States.GAME
    global timer
    timer = Timer("sprites/numbers.png")
    # Delay prevents multiple clicks from registering
    pygame.time.delay(250)


def quit_button_clicked():
    """Exits the game."""
    if quit_button.check_clicked():
        pygame.quit()
        raise SystemExit


while True:
    frame = pygame.time.get_ticks() // 500
    screen.blit(background, (0, 0))

    # displays title screen
    match state:
        case States.TITLE:
            title.play_animation(screen, frame, (66, 66))
            play_button.draw(frame, (48, 186))
            quit_button.draw(frame, (272, 186))
            play_button_clicked()
            quit_button_clicked()

        case States.SELECTION:
            random_button.draw(frame, (128, 48))
            human_button.draw(frame, (128, 192))
            insane_button.draw(frame, (128, 336))
            if random_button.check_clicked():
                selection_clicked()
                game_board = Board((160, 160), computers.RandomComputer())
            if human_button.check_clicked():
                selection_clicked()
                game_board = Board((160, 160), computers.HumanComputer())

        case States.GAME_OVER:
            game_board.display_board(screen, frame)

            # Displays win/lose/tie
            if game_board.check_win() is Moves.PLAYER:
                win.play_animation(screen, frame, (66, 12))
            elif game_board.check_win() is Moves.COMPUTER:
                lose.play_animation(screen, frame, (66, 12))
            elif game_board.is_board_full():
                tie.play_animation(screen, frame, (66, 12))

            play_button.draw(frame, (48, 372))
            quit_button.draw(frame, (272, 372))
            play_button_clicked()
            quit_button_clicked()

        case States.GAME:
            game_board.draw_board(screen, frame)
            quit_button.draw(frame, (272, 372))
            timer.display_timer(screen)
            quit_button_clicked()
            if game_board.check_win() is not Moves.NONE or game_board.is_board_full():
                state = States.GAME_OVER

    # Allows user to close program using the "X" button in the windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()
    clock.tick(30)
