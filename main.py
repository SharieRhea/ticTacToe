import pygame
import spritesheet
import button
import board

pygame.init()

screen = pygame.display.set_mode((500, 500))
BG = (50, 50, 50)

play_button = button.Button(spritesheet.SpriteSheet("sprites/play.png", 2, 48, 32, 4, (0, 0, 0)))

board = board.Board()

playing = False
while True:
    screen.fill(BG)

    if not playing:
        play_button.sprite.play_animation(screen, (154, 186))
        if play_button.check_clicked():
            playing = True
            # Delay prevents multiple clicks from registering
            pygame.time.delay(250)
    else:
        board.draw_board(screen)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()
