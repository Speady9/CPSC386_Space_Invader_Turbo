import pygame
from pygame.sprite import Sprite


class UFO(Sprite):
    """A class to represent a single alien in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(UFO, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.activate = False  # Flag used to trigger UFO movement

        # Load the UFO image and set its rect attribute.
        self.image = pygame.image.load('sprites/UFO.png')
        self.rect = self.image.get_rect()

        # Start the UFO behind the top left of the screen.
        self.rect.x = -self.rect.width
        self.rect.y = self.rect.height * 3

        # Store the alien's exact position.
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien and its current location."""
        self.screen.blit(self.image, self.rect)

    def reset(self):
        self.activate = False
        self.rect.x = -self.rect.width
        self.rect.y = self.rect.height * 3

    def update(self):
        """Move the UFO across the screen, once activated."""
        if self.activate:
            self.x += self.ai_settings.ufo_speed_factor
            self.rect.x = self.x
