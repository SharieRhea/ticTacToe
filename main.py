import pygame
import spritesheet

pygame.init()

screen = pygame.display.set_mode((500, 500))
BG = (50, 50, 50)
black = (0, 0, 0)

spriteSheetImage = pygame.image.load("sprites/X.png").convert_alpha()
spriteSheet = spritesheet.SpriteSheet(spriteSheetImage)

animation_list = []
animation_steps = 2
last_update = pygame.time.get_ticks()
animation_cooldown = 500
frame = 0

for x in range(animation_steps):
    animation_list.append(spriteSheet.get_image(x, 16, 16, 4, black))

while True:
    screen.fill(BG)

    current_time = pygame.time.get_ticks()
    if current_time - last_update >= animation_cooldown:
        frame += 1
        last_update = current_time
        if frame >= len(animation_list):
            frame = 0
    screen.blit(animation_list[frame], (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit

    pygame.display.update()
