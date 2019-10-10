import pygame

from pygame.sprite import Sprite


class EnemyBullet(Sprite):
    """A class to manage bullets fired from the enemy"""

    def __init__(self, ai_settings, screen, alien):
        """Create a bullet object at an alien's current position."""
        super().__init__()
        self.screen = screen

        # Create a bullet rect at (0, 0) and then set correct position.
        self.image = pygame.image.load('sprites/enemy_bullet.png')
        self.rect = self.image.get_rect
        self.rect.centerx = alien.rect.centerx
        self.rect.bottom = alien.rect.bottom

        # Store the bullet's position as a decimal value.
        self.y = float(self.rect.y)

        # self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """Move the bullet down the screen."""
        # Update the decimal position of the bullet.
        self.y -= self.speed_factor
        # Update the rect position.
        self.rect.y += self.speed_factor

    def draw_bullet(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
