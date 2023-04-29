import pygame


class SpriteSheet:
    """Models a sprite-sheet that may contain one or more frames of an animation in a line. Automatically creates a list
    of animation frames and initializes variables for an animation loop."""

    def __init__(self, file, frames, width, height, scale, color):
        """Initialize a sprite-sheet with necessary attributes."""
        # Basic attributes
        self.frames = frames
        self.width = width
        self.height = height
        self.scale = scale
        self.color = color

        self.sheet = pygame.image.load(file).convert_alpha()
        self.rect = pygame.Rect(0, 0, width * scale, height * scale)

        # Animation attributes
        self.animation_list = []
        self.last_update = pygame.time.get_ticks()
        self.animation_cooldown = 500
        self.frame = 0

        self.create_animation()

    def get_frame(self, frame):
        """Returns a specific frame of the sprite-sheet"""
        image = pygame.Surface((self.width, self.height)).convert_alpha()
        image.blit(self.sheet, (0, 0), (frame * self.width, 0, self.width, self.height))
        image = pygame.transform.scale(image, (self.width * self.scale, self.height * self.scale))
        image.set_colorkey(self.color)
        self.rect = image.get_rect()
        return image

    def create_animation(self):
        """Stores each frame of the sprite-sheet into a list."""
        animation_steps = self.frames

        for x in range(animation_steps):
            self.animation_list.append(self.get_frame(x))

    def play_animation(self, screen, location):
        """Plays the animations frames in order, looping back to frame0 when necessary."""
        current_time = pygame.time.get_ticks()
        if current_time - self.last_update >= self.animation_cooldown:
            self.frame += 1
            self.last_update = current_time
            if self.frame >= len(self.animation_list):
                self.frame = 0

        # Draw animation frame and update the rect for collision.
        screen.blit(self.animation_list[self.frame], location)
        self.rect.update(location[0], location[1], self.width * self.scale, self.height * self.scale)
