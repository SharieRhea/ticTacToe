import pygame


class Button:
    """Models an animated button that may perform different actions."""

    def __init__(self, screen, sprite, sprite_highlighted, location):
        """Initializes a button object."""
        self.screen = screen
        self.sprite = sprite
        self.sprite_highlighted = sprite_highlighted
        self.location = location

    def draw(self):
        if self.sprite.rect.collidepoint(pygame.mouse.get_pos()):
            self.sprite_highlighted.play_animation(self.screen, self.location)
        else:
            self.sprite.play_animation(self.screen, self.location)

    def check_clicked(self):
        """Returns True if the button is being clicked at that moment."""
        if self.sprite.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                return True
