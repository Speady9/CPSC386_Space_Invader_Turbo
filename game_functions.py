import sys
import pygame
import random

from alien import Alien1
from alien import Alien2
from alien import Alien3
from ship_bullet import ShipBullet
from time import sleep


def change_fleet_direction(ai_settings, aliens):
    """Drop the entire fleet and change the fleet's direction."""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def check_aliens_bottom(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets):
    """Check if any aliens have reached the bottom of the screen."""
    screen_rect = screen.get_rect()
    for alien1 in alien1.sprites():
        if alien1.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets)
            break
    for alien2 in alien2.sprites():
        if alien2.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets)
            break
    for alien3 in alien3.sprites():
        if alien3.rect.bottom >= screen_rect.bottom:
            # Treat this the same as if the ship got hit.
            ship_hit(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets)
            break


def check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, alien1, alien2, alien3, ufo, bullets):
    """Respond to the bullet-alien collisions."""
    # Remove any bullets and aliens that have collided.
    collisions1 = pygame.sprite.groupcollide(bullets, alien1, True, True)
    collisions2 = pygame.sprite.groupcollide(bullets, alien2, True, True)
    collisions3 = pygame.sprite.groupcollide(bullets, alien3, True, True)
    collisions_ufo = pygame.sprite.spritecollide(bullets, ufo, True, True)

    if collisions1:
        Alien1.explode(alien1)
        for alien1 in collisions1.values():
            ai_settings.hitSound.play()
            stats.score += ai_settings.alien1_points * len(alien1)
            sb.prep_score()
        check_high_score(stats, sb)
    if collisions2:
        Alien2.explode(alien2)
        for alien2 in collisions2.values():
            ai_settings.hitSound.play()
            stats.score += ai_settings.alien2_points * len(alien2)
            sb.prep_score()
        check_high_score(stats, sb)
    if collisions3:
        Alien3.explode(alien3)
        for alien3 in collisions3.values():
            ai_settings.hitSound.play()
            stats.score += ai_settings.alien3_points * len(alien3)
            sb.prep_score()
        check_high_score(stats, sb)
    if collisions_ufo:  # Grants points between 50-200 (and increasing).
        stats.score += int(random.randint(5-20) * ai_settings.ufo_factor)

    if len(alien3) == 0:  # If bottom row is destroyed...
        if len(alien2) == 0:  # If middle row is destroyed...
            if len(alien1) == 0:  # If top row is destroyed...
                # If the entire fleet is destroyed, start a new level.
                bullets.empty()
                ai_settings.increase_speed()

                # Increase level.
                stats.level += 1
                sb.prep_level()

                ufo.__init__(ai_settings, screen)

                create_fleet1(ai_settings, screen, alien1)
                create_fleet2(ai_settings, screen, alien2)
                create_fleet3(ai_settings, screen, alien3)


def check_events(ai_settings, screen, stats, sb, play_button, ship, alien1, alien2, alien3, ufo, ship_bullets, enemy_bullets):
    """Respond to key presses and mouse events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, ship_bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ai_settings, screen, ship, ship_bullets)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, stats, sb, play_button, ship, alien1, alien2, alien3, ufo,\
                              ship_bullets, enemy_bullets, mouse_x, mouse_y)


def check_fleet_edges(ai_settings, aliens):
    """Respond appropriately if any aliens have reached an edge."""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def check_high_score(stats, sb):
    """Check to see if there's a new high score."""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """Respond to key presses."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ai_settings, screen, ship, bullets):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    if event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_play_button(ai_settings, screen, stats, sb, play_button, ship, alien1, alien2, alien3,
                      ufo, ship_bullets, enemy_bullets, mouse_x, mouse_y):
    """Start a new game when the player clicks Play."""
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # Reset the game settings.
        ai_settings.initialize_dynamic_settings()

        # Hide the mouse cursor.
        pygame.mouse.set_visible(False)

        # Reset the game statistics.
        stats.reset_stats()
        stats.game_active = True

        # Reset the scoreboard images.
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # Empty the list of aliens and bullets.
        alien1.empty()
        alien2.empty()
        alien3.empty()
        ship_bullets.empty()
        enemy_bullets.empty()
        ufo.empty()

        # Create a new fleet and center the ship.
        create_fleet1(ai_settings, screen, alien1)
        create_fleet2(ai_settings, screen, alien2)
        create_fleet3(ai_settings, screen, alien3)
        ship.center_ship()


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """Create an alien and place it in a row."""
    global alien

    if row_number == 1:
        alien = Alien1(ai_settings, screen)
    if row_number == 2:
        alien = Alien2(ai_settings, screen)
    if row_number == 3:
        alien = Alien3(ai_settings, screen)

    alien_width = alien.rect.width
    alien.x = alien_width + (2 * alien_width * alien_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + (2 * alien.rect.height * row_number)
    aliens.add(alien)


def create_fleet1(ai_settings, screen, aliens):
    """Create a full fleet of aliens on the top row."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien1 = Alien1(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien1.rect.width)
    # number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number, 1)


def create_fleet2(ai_settings, screen, aliens):
    """Create a full fleet of aliens on the middle row."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien2 = Alien2(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien2.rect.width)
    # number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number, 2)


def create_fleet3(ai_settings, screen, aliens):
    """Create a full fleet of aliens on the bottom row."""
    # Create an alien and find the number of aliens in a row.
    # Spacing between each alien is equal to one alien width.
    alien3 = Alien3(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien3.rect.width)
    # number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    # Create the fleet of aliens.
    for alien_number in range(number_aliens_x):
        create_alien(ai_settings, screen, aliens, alien_number, 3)


def fire_bullet(ai_settings, screen, ship, ship_bullets):
    """Fire a bullet if limit is not reached yet."""
    # Create a new bullet and add it to the bullets group.
    if len(ship_bullets) < ai_settings.bullets_allowed:
        ai_settings.shootSound.play()
        new_bullet = ShipBullet(ai_settings, screen, ship)
        ship_bullets.add(new_bullet)


def get_number_aliens_x(ai_settings, alien_width):
    """Determine the number of aliens that fit in a row."""
    available_space_x = ai_settings.screen_width - (2 * alien_width)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def get_number_rows(ai_settings, ship_height, alien_height):
    """Determine the number of rows of aliens that fit on the screen."""
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def ship_hit(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets):
    """Respond to ship being hit by alien."""
    if stats.ships_left > 0:
        # Decrement ships left.
        stats.ships_left -= 1

        # Empty the list of aliens and bullets.
        alien1.empty()
        alien2.empty()
        alien3.empty()
        ship_bullets.empty()
        ufo.reset()
        # enemy_bullets.empty()

        # Create a new fleets and center the ship.
        create_fleet1(ai_settings, screen, alien1)
        create_fleet2(ai_settings, screen, alien2)
        create_fleet3(ai_settings, screen, alien3)
        ship.center_ship()

        # Update scoreboard.
        sb.prep_ships()

        # Pause and play death sound.
        ai_settings.dieSound.play()
        sleep(2.0)

    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def update_aliens(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets):
    """
    Check if the fleet is at an edge,
    and then update the positions of all aliens in the fleet.
    """
    check_fleet_edges(ai_settings, alien1)
    check_fleet_edges(ai_settings, alien2)
    check_fleet_edges(ai_settings, alien3)
    alien1.update()
    alien2.update()
    alien3.update()
    ufo.update()

    # UFO algorithm
    ufo_trigger = random.randint(0, 1000)
    if ufo_trigger == 500:
        ufo.activate = True  # UFO is sent on-screen once the random generator hits 500

    # Look for alien-ship collisions.
    if pygame.sprite.spritecollideany(ship, alien1):
        ship_hit(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets)
    if pygame.sprite.spritecollideany(ship, alien2):
        ship_hit(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets)
    if pygame.sprite.spritecollideany(ship, alien3):
        ship_hit(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets)

    # Look for aliens hitting the bottom of the screen.
    check_aliens_bottom(ai_settings, stats, sb, screen, ship, alien1, alien2, alien3, ufo, ship_bullets)


def update_alien_bullets(ai_settings, screen, stats, sb, ship, alien1, alien2, alien3, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, alien1, alien2, alien3, bullets)


def update_ship_bullets(ai_settings, screen, stats, sb, ship, alien1, alien2, alien3, ufo, bullets):
    """Update position of bullets and get rid of old bullets."""
    # Update bullet positions.
    bullets.update()

    # Get rid of bullets that have disappeared.
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(ai_settings, screen, stats, sb, ship, alien1, alien2, alien3, ufo, bullets)


def update_screen(ai_settings, screen, stats, sb, ship, alien1, alien2, alien3, ufo, ship_bullets, enemy_bullets, play_button):
    """Update images on screen and flip to the new screen."""
    # Redraw the screen during each pass through the loop.
    screen.blit(ai_settings.bg_image, ai_settings.back_rect)

    # Redraw all bullets behind ship and aliens.
    for ship_bullet in ship_bullets.sprites():
        ship_bullet.draw_bullet()
    for enemy_bullet in enemy_bullets.sprites():
        enemy_bullet.draw_bullet()

    ship.blitme()
    alien1.draw(screen)
    alien2.draw(screen)
    alien3.draw(screen)
    ufo.draw(screen)

    # Draw the score information.
    sb.show_score()

    # Draw the play button if the game is inactive.
    if not stats.game_active:
        play_button.draw_button()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
