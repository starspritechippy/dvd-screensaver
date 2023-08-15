# Example file showing a basic pygame "game loop"
import pygame
import simpleaudio as sa
from classes.sprite import Sprite


class Line:
    point_a: tuple[float, float]
    point_b: tuple[float, float]

    def __init__(
        self, point_a: tuple[float, float], point_b: tuple[float, float]
    ) -> None:
        self.point_a = point_a
        self.point_b = point_b


# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
screen_rect = screen.get_rect()
clock = pygame.time.Clock()
running = True

dvd_sprite = Sprite("assets/dvd-cropped.png", (400, 400), scale_factor=0.2)
dvd_movement = pygame.Vector2(-2, -2)  # .normalize()

yippie_sound = sa.WaveObject.from_wave_file("assets/yippie.wav")

while running:
    screen_rect = screen.get_rect()
    screen_borders = (
        Line(screen_rect.topleft, screen_rect.topright),
        Line(screen_rect.bottomleft, screen_rect.bottomright),
        Line(screen_rect.topright, screen_rect.bottomright),
        Line(screen_rect.topleft, screen_rect.bottomleft),
    )
    corners_hit = 0

    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    # spawn dvd logo
    dvd_sprite.draw(screen)

    # now move it up right
    if not dvd_sprite.move(dvd_movement, screen.get_rect()):
        if dvd_sprite.simulate_move(dvd_movement).clipline(
            screen_borders[0].point_a, screen_borders[0].point_b
        ):
            # top line clipped
            dvd_movement = dvd_movement.reflect(pygame.Vector2(0, -1))
            dvd_sprite.change_color()
            corners_hit += 1
        if dvd_sprite.simulate_move(dvd_movement).clipline(
            screen_borders[1].point_a, screen_borders[1].point_b
        ):
            # bottom line clipped

            dvd_movement = dvd_movement.reflect(pygame.Vector2(0, -1))
            dvd_sprite.change_color()
            corners_hit += 1
        if dvd_sprite.simulate_move(dvd_movement).clipline(
            screen_borders[2].point_a, screen_borders[2].point_b
        ):
            # right line clipped
            dvd_movement = dvd_movement.reflect(pygame.Vector2(-1, 0))
            dvd_sprite.change_color()
            corners_hit += 1
        if dvd_sprite.simulate_move(dvd_movement).clipline(
            screen_borders[3].point_a, screen_borders[3].point_b
        ):
            # left line clipped
            dvd_movement = dvd_movement.reflect(pygame.Vector2(-1, 0))
            dvd_sprite.change_color()
            corners_hit += 1

    if corners_hit > 1:
        yippie_sound.play()

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
