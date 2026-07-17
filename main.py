import pygame
from pygame.locals import *

# Initialise Pygame
pygame.init()

# Create a display window
screen = pygame.display.set_mode((800, 600))

# Create a clock object
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Drawing
    screen.fill((0, 255, 255))
    pygame.display.update()

    # Limit frame rate to 60fps
    clock.tick(60)

pygame.quit()
