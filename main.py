import pygame
import spritesheet

pygame.init()

screen = pygame.display.set_mode((500, 500))
BG = (50, 50, 50)
black = (0, 0, 0)

X = spritesheet.SpriteSheet(spritesheet.load_image("sprites/X.png"))
X.create_animation(2, 16, 16, 4)

while True:
    screen.fill(BG)

    X.play_animation(screen, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.update()
