import pygame


def load_image(file):
    return pygame.image.load(file).convert_alpha()


class SpriteSheet:
    def __init__(self, image):
        self.animation_list = []
        self.sheet = image
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 500
        self.frame = 0

    def get_frame(self, frame, width, height, scale, color):
        image = pygame.Surface((width, height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        image = pygame.transform.scale(image, (width * scale, height * scale))
        image.set_colorkey(color)
        return image

    def create_animation(self, frames, width, height, scale):
        alpha = (0, 0, 0)
        animation_steps = frames

        for x in range(animation_steps):
            self.animation_list.append(self.get_frame(x, width, height, scale, alpha))

    def play_animation(self, screen, location):
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list):
                self.frame = 0
        screen.blit(self.animation_list[self.frame], location)
