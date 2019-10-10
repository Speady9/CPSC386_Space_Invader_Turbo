# Space Invader Turbo
# Project by Hunter Gerace
# CPSC 386
# 11 October 2019

import sys
import pygame
from alien import Alien1
from alien import Alien2
from alien import Alien3
from ufo import UFO
from button import Button
from game_stats import GameStats
from pygame.sprite import Group
from scoreboard import Scoreboard
from settings import Settings
from ship import Ship
import game_functions as gf


def run_game():
    # Initialize pygame, settings, and screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Space Invader Turbo")

    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # Make a ship, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    ship_bullets = Group()
    enemy_bullets = Group()
    alien1 = Group()
    alien2 = Group()
    alien3 = Group()
    ufo = Group()

    # Create the fleets of aliens.
    gf.create_fleet1(ai_settings, screen, alien1)
    gf.create_fleet2(ai_settings, screen, alien2)
    gf.create_fleet3(ai_settings, screen, alien3)

    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, alien1, alien2, alien3, ufo,\
                        ship_bullets, enemy_bullets)

        if stats.game_active:
            ship.update()
            gf.update_ship_bullets(ai_settings, screen, stats, sb, ship, alien1, alien2, alien3, ufo, ship_bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets)

        gf.update_screen(ai_settings, screen, stats, sb, ship, alien1, alien2, alien3, ufo, ship_bullets, enemy_bullets, play_button)


run_game()
