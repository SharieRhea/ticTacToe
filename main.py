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
instructions_regular = SpriteSheet("sprites/instructions.png", 1, 96, 32, 4, alpha)
instructions_highlighted = SpriteSheet("sprites/instructionsHighlighted.png", 2, 96, 32, 4, alpha)
instructions_button = Button(screen, instructions_regular, instructions_highlighted)
random_regular = SpriteSheet("sprites/random.png", 1, 64, 32, 4, alpha)
random_highlighted = SpriteSheet("sprites/randomHighlighted.png", 2, 64, 32, 4, alpha)
random_button = Button(screen, random_regular, random_highlighted)
human_regular = SpriteSheet("sprites/human.png", 1, 64, 32, 4, alpha)
human_highlighted = SpriteSheet("sprites/humanHighlighted.png", 2, 64, 32, 4, alpha)
human_button = Button(screen, human_regular, human_highlighted)
insane_regular = SpriteSheet("sprites/insane.png", 1, 64, 32, 4, alpha)
insane_highlighted = SpriteSheet("sprites/insaneHighlighted.png", 2, 64, 32, 4, alpha)
insane_button = Button(screen, insane_regular, insane_highlighted)
secret_regular = SpriteSheet("sprites/secret.png", 1, 48, 32, 4, alpha)
secret_highlighted = SpriteSheet("sprites/secretHighlighted.png", 2, 48, 32, 4, alpha)
secret_button = Button(screen, secret_regular, secret_highlighted)

my_font = pygame.font.SysFont("Minecraftia", 18)
instructions_text = [my_font.render("How to Play:", False, (255, 255, 255)),
                     my_font.render("   You will plays as 'X' and the computer", False, (255, 255, 255)),
                     my_font.render("   will play as 'O'.", False, (255, 255, 255)),
                     my_font.render("   Starting with you, each player will take", False, (255, 255, 255)),
                     my_font.render("   turns placing their symbol in a square.", False, (255, 255, 255)),
                     my_font.render("   A player wins when they have three of", False, (255, 255, 255)),
                     my_font.render("   their own symbols in a row.", False, (255, 255, 255)),
                     my_font.render("", False, (0, 0, 0)),
                     my_font.render("Types of Computers:", False, (255, 255, 255)),
                     my_font.render("   Random: Will play a random move every turn.", False, (255, 255, 255)),
                     my_font.render("   Human: Will play a move to win or block ", False, (255, 255, 255)),
                     my_font.render("   you from winning. If this isn't an ", False, (255, 255, 255)),
                     my_font.render("   option, plays a random move.", False, (255, 255, 255)),
                     my_font.render("   Insane: Will play the move that ", False, (255, 255, 255)),
                     my_font.render("   statistically leads to the most wins.", False, (255, 255, 255))]

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


def instructions_button_clicked():
    """Changes the state to reflect displaying the instructions screen."""
    if instructions_button.check_clicked():
        global state
        state = States.INSTRUCTIONS


while True:
    frame = pygame.time.get_ticks() // 500
    screen.blit(background, (0, 0))

    # displays title screen
    match state:
        case States.TITLE:
            title.play_animation(screen, frame, (66, 66))
            play_button.draw(frame, (48, 186))
            quit_button.draw(frame, (272, 186))
            instructions_button.draw(frame, (66, 306))
            play_button_clicked()
            quit_button_clicked()
            instructions_button_clicked()

        case States.INSTRUCTIONS:
            height = 20
            for text in instructions_text:
                screen.blit(text, (10, height))
                height += 25
            play_button.draw(frame, (48, 390))
            quit_button.draw(frame, (272, 390))
            play_button_clicked()
            if quit_button.check_clicked():
                state = States.TITLE
                pygame.time.delay(250)

        case States.SELECTION:
            random_button.draw(frame, (128, 48))
            human_button.draw(frame, (128, 192))
            insane_button.draw(frame, (128, 336))
            secret_button.draw(frame, (363, 420))
            if random_button.check_clicked():
                selection_clicked()
                game_board = Board((160, 160), computers.RandomComputer())
            if human_button.check_clicked():
                selection_clicked()
                game_board = Board((160, 160), computers.HumanComputer())
            if insane_button.check_clicked():
                selection_clicked()
                game_board = Board((160, 160), computers.InsaneComputer())
            if secret_button.check_clicked():
                selection_clicked()
                game_board = Board((160, 160), computers.SecretComputer())

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
            if quit_button.check_clicked():
                state = States.TITLE
                pygame.time.delay(250)
            if game_board.check_win() is not Moves.NONE or game_board.is_board_full():
                state = States.GAME_OVER

    # Allows user to close program using the "X" button in the windows
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()
    clock.tick(30)
