import pygame


class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""

        # Alien settings
        self.fleet_drop_speed = 10

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 0, 0, 0
        self.bullets_allowed = 3

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        # Screen settings
        self.screen_width = 560
        self.screen_height = 640
        self.bg_image = pygame.image.load('sprites/background.png')
        self.back_rect = pygame.Rect(0, 0, 560, 640)

        # Ship settings
        self.ship_limit = 3

        # Shield settings
        self.shield_height = 32
        self.shield_width = 32
        self.shield_color = (0, 255, 0)

        # Music and sound prep
        pygame.mixer.pre_init(44100, 16, 2, 4096)
        self.hitSound = pygame.mixer.Sound('sounds/alien_kill.wav')
        self.shootSound = pygame.mixer.Sound('sounds/ship_shoot.wav')
        self.dieSound = pygame.mixer.Sound('sounds/death.wav')
        pygame.mixer.music.load('sounds/alien_invasion.mp3')
        # pygame.mixer.music.set_volume(0.25)
        pygame.mixer.music.play(-1, 0.0)
        musicPlaying = True

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 3
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.ufo_speed_factor = 0.75

        # Fleet direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring
        self.alien1_points = 40
        self.alien2_points = 20
        self.alien3_points = 10
        self.ufo_factor = 10  # Allows random UFO scoring to adjust to increase.

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        # self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.ufo_speed_factor *= self.speedup_scale

        self.alien1_points = int(self.alien1_points * self.score_scale)
        self.alien2_points = int(self.alien2_points * self.score_scale)
        self.alien3_points = int(self.alien3_points * self.score_scale)
        self.ufo_factor = int(self.ufo_factor * self.score_scale)
