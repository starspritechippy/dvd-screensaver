# Example file showing a basic pygame "game loop"
import pygame
from classes.sprite import Sprite

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

dvd_image = pygame.image.load("assets/dvd-cropped.png").convert_alpha()
dvd_image_resized = pygame.transform.smoothscale_by(dvd_image, 0.1)

dvd_sprite = Sprite("assets/dvd-cropped.png", (400, 400), scale_factor=0.1)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("white")

    # RENDER YOUR GAME HERE
    dvd_sprite.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()
