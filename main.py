import pygame
import spritesheet
import button
import board

pygame.init()

screen = pygame.display.set_mode((512, 512))
BG = (50, 50, 50)
alpha = (0, 0, 0)

title = spritesheet.SpriteSheet("sprites/ticTacToe.png", 7, 96, 48, 4, alpha)

play_regular = spritesheet.SpriteSheet("sprites/play.png", 2, 48, 32, 4, alpha)
play_highlighted = spritesheet.SpriteSheet("sprites/playHighlighted.png", 2, 48, 32, 4, alpha)
play = button.Button(screen, play_regular, play_highlighted, (48, 186))

quit_regular = spritesheet.SpriteSheet("sprites/quit.png", 2, 48, 32, 4, alpha)
quit_highlighted = spritesheet.SpriteSheet("sprites/quitHighlighted.png", 2, 48, 32, 4, alpha)
quit_button = button.Button(screen, quit_regular, quit_highlighted, (272, 186))

board = board.Board()

playing = False
while True:
    screen.fill(BG)

    if not playing:
        title.play_animation(screen, (66, 66))
        play.draw()
        quit_button.draw()
        if play.check_clicked():
            playing = True
            # Delay prevents multiple clicks from registering
            pygame.time.delay(250)
        if quit_button.check_clicked():
            pygame.quit()
            raise SystemExit

    else:
        if board.is_board_full():
            pygame.quit()
            raise SystemExit
        else:
            board.draw_board(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()
