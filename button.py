import pygame


class Button:
    """Models an animated button that may perform different actions."""

    def __init__(self, sprite):
        """Initializes a button object."""
        self.sprite = sprite
        self.hover = False
        self.clicked = False

    def check_clicked(self):
        """Returns True if the button is being clicked at that moment."""
        self.hover = False
        self.clicked = False
        if self.sprite.rect.collidepoint(pygame.mouse.get_pos()):
            self.hover = True
            if pygame.mouse.get_pressed()[0]:
                self.clicked = True

        return self.clicked
