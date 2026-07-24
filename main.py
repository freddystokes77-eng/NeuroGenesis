from simulation.world import World
from simulation.creature import Creature
from simulation.food import Food
from simulation.genome import Genome
import pygame
from pygame.locals import *
import random
import numpy as np

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

# Returns a new world object
# Takes a list of creatures as input
def new_generation(creatures):
    food = []

    for i in range(20):
        x = random.randint(405, 770)
        y = random.randint(30, 395)
        food.append(Food(RED, (x, y), 5))
        
    return World(400, 25, 375, 375, (0, 255, 0), 
        food, 
        creatures)

def simulateGeneration(world, screen):
    # Drawing
    screen.fill((0, 255, 255))
    world.draw_world(screen)
    for creature in world.creatures:
        if creature.isAlive:
            creature.move(world)
    
    world.draw_creatures(screen)
    world.draw_food(screen)

# Create a world object
creatures = []

for i in range(50):
    speed = random.uniform(0.01,0.5)
    visionRadius = random.uniform(5,25)
    energyEfficiency = random.uniform(20,80)
    size = random.randint(1,5)
    weights = np.random.randn(42)
    x = random.randint(400 + size, 775 - size)
    y = random.randint(25 + size, 400 - size)
    creatures.append(Creature(Genome(speed, visionRadius, energyEfficiency, size, weights), BLUE, (x, y), 100, True))

    
world = new_generation(creatures)

# Create a timer
startTime = 0
currentTime = 0
duration = 15000

# Create a generation counter
genCount = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    currentTime = pygame.time.get_ticks()
    if currentTime - startTime >= duration:
        print("End of generation", genCount)
        world.get_average_stats()
        newCreatures = world.mutate_generation()
        world = new_generation(newCreatures)
        startTime = currentTime
        genCount += 1
        
    simulateGeneration(world, screen)
    
    pygame.display.update()

    # Limit frame rate to 60fps
    clock.tick(60)

pygame.quit()
