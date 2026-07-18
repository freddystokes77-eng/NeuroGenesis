from simulation.world import World
from simulation.creature import Creature
from simulation.food import Food
import pygame
from pygame.locals import *

# Initialise Pygame
pygame.init()

# Create a display window
screen = pygame.display.set_mode((800, 600))

# Create a clock object
clock = pygame.time.Clock()

# Define colours
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create a world object
w1 = World(400, 25, 375, 375, (0, 255, 0), [Food(RED, (750, 250), 10), Food(RED, (650, 150), 5), Food(RED, (650, 200), 5)], [Creature(BLUE, (700, 200), 5, 5, 100, True)])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Drawing
    screen.fill((0, 255, 255))
    w1.draw_world(screen)
    for creature in w1.creatures:
        creature.move(w1)
        creature.drain_energy()
    
    w1.draw_creatures(screen)
    w1.draw_food(screen)
    pygame.display.update()

    # Limit frame rate to 60fps
    clock.tick(60)

pygame.quit()
