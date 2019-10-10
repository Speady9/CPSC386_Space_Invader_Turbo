import pygame
from pygame.sprite import Sprite


class Shield(Sprite):
    def __init__(self, ai_settings, screen):
        super(Shield, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.height = ai_settings.shield_height
        self.width = ai_settings.shield_width
        self.color = ai_settings.shield_color
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

    def blitme(self):
        """Draw the alien and its current location."""
        self.screen.blit(self.image, self.rect)
