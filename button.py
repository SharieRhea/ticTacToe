import os
import sys

import pygame


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


class Button:
    """Models an animated button that may perform different actions."""

    def __init__(self, screen, sprite, sprite_highlighted):
        """Initializes a button object."""
        self.screen = screen
        self.sprite = sprite
        self.sprite_highlighted = sprite_highlighted
        self.sfx = pygame.mixer.Sound(resource_path("audio/switch2.ogg"))

    def draw(self, frame, location):
        """Displays the current state of the button (normal/hovered)."""
        if self.sprite.rect.collidepoint(pygame.mouse.get_pos()):
            self.sprite_highlighted.play_animation(self.screen, frame, location)
        else:
            self.sprite.play_animation(self.screen, frame, location)

    def check_clicked(self):
        """Returns True if the button is being clicked at that moment."""
        if self.sprite.rect.collidepoint(pygame.mouse.get_pos()):
            if pygame.mouse.get_pressed()[0]:
                self.sfx.play()
                return True
