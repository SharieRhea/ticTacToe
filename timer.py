import pygame


class Timer:
    """Models a timer with minutes and seconds."""
    def __init__(self, file):
        """Initializes a timer."""
        self.file = file
        self.size = 16
        self.scale = 4
        self.color = (0, 0, 0)
        self.start_time = pygame.time.get_ticks()

        self.sheet = pygame.image.load(file).convert_alpha()

    def get_frame(self, index):
        """Returns a specific number/symbol."""
        image = pygame.Surface((self.size, self.size)).convert_alpha()
        image.blit(self.sheet, (0, 0), (index * self.size, 0, self.size, self.size))
        image = pygame.transform.scale(image, (self.size * self.scale, self.size * self.scale))
        image.set_colorkey(self.color)
        return image

    def display_timer(self, screen):
        """Gets the current values for minutes and seconds and displays those values to the screen."""
        ticks = pygame.time.get_ticks() - self.start_time

        minutes = int((ticks / 1000) / 60)
        seconds = int((ticks / 1000) % 60)

        # Splits minutes and seconds into digits for use as indices
        minute_digits = [int(digit) for digit in str(minutes).zfill(2)]
        second_digits = [int(digit) for digit in str(seconds).zfill(2)]
        # alternate way: second_digits = list(map(int, str(seconds).zfill(2)))

        if minutes > 99:
            screen.blit(self.get_frame(9), (16, 410))
            screen.blit(self.get_frame(9), (64, 410))
            screen.blit(self.get_frame(10), (112, 410))
            screen.blit(self.get_frame(9), (160, 410))
            screen.blit(self.get_frame(9), (208, 410))
        else:
            screen.blit(self.get_frame(minute_digits[0]), (16, 410))
            screen.blit(self.get_frame(minute_digits[1]), (64, 410))
            screen.blit(self.get_frame(10), (112, 410))
            screen.blit(self.get_frame(second_digits[0]), (160, 410))
            screen.blit(self.get_frame(second_digits[1]), (208, 410))
