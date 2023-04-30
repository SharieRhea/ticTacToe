import pygame
import spritesheet
import button
import board

pygame.init()
clock = pygame.time.Clock()

screen = pygame.display.set_mode((512, 512))
BG = (50, 50, 50)
alpha = (0, 0, 0)

background = pygame.image.load("sprites/background.png")

title = spritesheet.SpriteSheet("sprites/ticTacToe.png", 7, 96, 48, 4, alpha)

play_regular = spritesheet.SpriteSheet("sprites/play.png", 1, 48, 32, 4, alpha)
play_highlighted = spritesheet.SpriteSheet("sprites/playHighlighted.png", 2, 48, 32, 4, alpha)
play = button.Button(screen, play_regular, play_highlighted)

quit_regular = spritesheet.SpriteSheet("sprites/quit.png", 1, 48, 32, 4, alpha)
quit_highlighted = spritesheet.SpriteSheet("sprites/quitHighlighted.png", 2, 48, 32, 4, alpha)
quit_button = button.Button(screen, quit_regular, quit_highlighted)

win = spritesheet.SpriteSheet("sprites/win.png", 2, 96, 48, 4, (0, 0, 0))
draw = spritesheet.SpriteSheet("sprites/draw.png", 2, 96, 48, 4, (0, 0, 0))
lose = spritesheet.SpriteSheet("sprites/loss.png", 2, 96, 48, 4, (0, 0, 0))

board = board.Board((160, 160))

playing = False
while True:
    screen.blit(background, (0, 0))

    if not playing:
        title.play_animation(screen, (66, 66))
        play.draw((48, 186))
        quit_button.draw((272, 186))
        if play.check_clicked():
            playing = True
            # Delay prevents multiple clicks from registering
            pygame.time.delay(250)
        if quit_button.check_clicked():
            pygame.quit()
            raise SystemExit

    else:
        board.draw_board(screen)
        if board.check_win():
            win.play_animation(screen, (66, 12))
            play.draw((48, 372))
            quit_button.draw((272, 372))
            if play.check_clicked():
                playing = True
                # Delay prevents multiple clicks from registering
                pygame.time.delay(250)
            if quit_button.check_clicked():
                pygame.quit()
                raise SystemExit
        elif board.is_board_full():
            draw.play_animation(screen, (66, 12))
            play.draw((48, 372))
            quit_button.draw((272, 372))
            if play.check_clicked():
                playing = True
                # Delay prevents multiple clicks from registering
                pygame.time.delay(250)
            if quit_button.check_clicked():
                pygame.quit()
                raise SystemExit

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()
    clock.tick(30)
