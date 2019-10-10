import pygame
from pygame.sprite import Sprite


class Alien1(Sprite):
    """A class to represent a single alien in the top fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien1, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.points = ai_settings.alien1_points

        # Load the alien image and set its rect attribute.
        self.images = [pygame.image.load('sprites/alien1_1.png'), pygame.image.load('sprites/alien1_2.png')]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 24)

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height * 4

    def blitme(self):
        """Draw the alien and its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def explode(self):
        self.image = [pygame.image.load('sprites/alien1_exp1.png'), pygame.image.load('sprites/alien1_exp2.png')]

    def update(self):
        """Move the alien right or left."""
        self.rect.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        # self.rect.x = self.x

        """Animate alien."""
        Clock.time += 1
        if Clock.time % 120 == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]


class Alien2(Sprite):
    """A class to represent a single alien in the middle fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien2, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.points = ai_settings.alien2_points

        # Load the alien image and set its rect attribute.
        self.images = [pygame.image.load('sprites/alien2_1.png'), pygame.image.load('sprites/alien2_2.png')]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 24)

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height * 5

    def blitme(self):
        """Draw the alien and its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def explode(self):
        self.image = [pygame.image.load('sprites/alien2_exp1.png'), pygame.image.load('sprites/alien2_exp2.png')]

    def update(self):
        """Move the alien right or left."""
        self.rect.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        # self.rect.x = self.x

        """Animate alien."""
        Clock.time += 1
        if Clock.time % 120 == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]


class Alien3(Sprite):
    """A class to represent a single alien in the bottom fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alien and set its starting position."""
        super(Alien3, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        self.points = ai_settings.alien3_points

        # Load the alien image and set its rect attribute.
        self.images = [pygame.image.load('sprites/alien3_1.png'), pygame.image.load('sprites/alien3_2.png')]
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(0, 0, 32, 24)

        # Start each new alien near the top left of the screen.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height * 6

    def blitme(self):
        """Draw the alien and its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alien is at the edge of the screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def explode(self):
        self.image = [pygame.image.load('sprites/alien3_exp1.png'), pygame.image.load('sprites/alien3_exp2.png')]

    def update(self):
        """Move the alien right or left."""
        self.rect.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        # self.rect.x = self.x

        """Animate alien."""
        Clock.time += 1
        if Clock.time % 120 == 0:
            self.index += 1
            if self.index >= len(self.images):
                self.index = 0
            self.image = self.images[self.index]

class Clock:
    time = 0