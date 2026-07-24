import pygame
import math
from simulation.brain.neural_brain import NeuralBrain

class Creature:
    def __init__(self, genome, colour, position, energy, isAlive):
        self.genome = genome
        self.brain = NeuralBrain(self, genome.weights)
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

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.genome.size)

    def drain_energy(self, currentSpeed):
        if self.energy <= 0:
            self.isAlive = False
            self.timeSurvived = pygame.time.get_ticks()
        else:
            percentageOfMaxSpeed = currentSpeed / self.genome.speed
            energyLost = 0.02 + ((0.04 * percentageOfMaxSpeed) / (self.genome.energyEfficiency / 100))
            #energyLost = 0.02 + ((0.03 * percentageOfMaxSpeed) / (self.genome.energyEfficiency / 100))
            self.energy -= energyLost
            self.energySpent += energyLost

    def gain_energy(self):
        self.energy += 15
        self.foodEaten += 15
        if self.energy > 100:
            self.energy = 100

    # def set_speed(self):
    #     speed = self.genome.speed
    #     self.speed_x, self.speed_y = self.brain.decide()

    def move(self, world):
        x, y = self.position
        direction = self.brain.decide(world)
        self.speed_x, self.speed_y = direction

        # Update position
        x += self.speed_x
        y += self.speed_y

        # Keep the circle fully inside the world bounds.
        min_x = world.left + self.genome.size
        max_x = world.left + world.width - self.genome.size
        min_y = world.top + self.genome.size
        max_y = world.top + world.height - self.genome.size

        if x <= min_x:
            x = min_x
            self.speed_x = abs(self.speed_x)
        elif x >= max_x:
            x = max_x
            self.speed_x = -abs(self.speed_x)

        if y <= min_y:
            y = min_y
            self.speed_y = abs(self.speed_y)
        elif y >= max_y:
            y = max_y
            self.speed_y = -abs(self.speed_y)

        self.position = x, y
        self.drain_energy(math.sqrt(self.speed_x**2 + self.speed_y**2))
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
        
                
                
