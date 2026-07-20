import pygame
import random
import math
from simulation.brain.base_brain import Brain

class Creature:
    def __init__(self, genome, colour, position, energy, isAlive):
        self.genome = genome
        self.brain = Brain(self)
        self.colour = colour
        self.position = position
        self.speed_x = 0
        self.speed_y = 0
        self.energy = energy
        self.isAlive = isAlive
        self.timeSurvived = 0
        self.energySpent = 0
        self.foodEaten = 0
        self.fitness = 0
        self.set_speed()

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.genome.size)

    def drain_energy(self):
        if self.energy <= 0:
            self.isAlive = False
            self.timeSurvived = pygame.time.get_ticks()
        else:
            energyLost =  0.1 / (self.genome.energyEfficiency / 100)
            self.energy -= energyLost
            self.energySpent += energyLost

    def gain_energy(self):
        self.energy += 5
        self.foodEaten += 5
        if self.energy > 100:
            self.energy = 100

    def set_speed(self):
        speed = self.genome.speed
        self.speed_x = random.uniform(-speed, speed)
        self.speed_y = math.sqrt(speed**2 - self.speed_x**2)

    def move(self, world):
        x, y = self.position
        direction = self.brain.decideDirection(world)
        self.speed_x, self.speed_y = direction
        
        # Update postion
        x += self.speed_x
        y += self.speed_y


        # Bounce off screen edges
        if x - self.genome.size <= world.left or x + self.genome.size >= world.left + world.width:
            self.speed_x *= -1
        if y - self.genome.size <= world.top or y + self.genome.size >= world.top + world.height:
            self.speed_y *= -1

        self.position = x, y
        self.checkForCollision(world)

    def checkForCollision(self, world):
        x1, y1 = self.position
        for food_item in world.food:
            x2, y2 = food_item.position
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if distance < self.genome.size + food_item.radius:
                world.food.remove(food_item)
                del food_item
                world.add_food()
                self.gain_energy()
        
                
                
