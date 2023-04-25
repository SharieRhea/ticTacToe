import pygame
import spritesheet
import button

pygame.init()

screen = pygame.display.set_mode((500, 500))
BG = (50, 50, 50)

board = pygame.image.load("sprites/board.png").convert_alpha()
board.set_colorkey((0, 0, 0))
board = pygame.transform.scale(board, (192, 192))

play_button = button.Button(spritesheet.SpriteSheet("sprites/play.png", 2, 48, 32, 4, (0, 0, 0)))

playing = False
while True:
    screen.fill(BG)

    if not playing:
        play_button.sprite.play_animation(screen, (154, 186))
        if play_button.check_clicked():
            playing = True
    else:
        screen.blit(board, (154, 154))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.flip()
