import pygame
from simulation.food import Food
from simulation.creature import Creature
import random

class World:
    def __init__(self, left, top, width, height, colour, food, creatures):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.colour = colour
        self.food = food
        self.creatures = creatures
    
    def draw_world(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.left, self.top, self.width, self.height))
    
    def draw_creatures(self, screen):
        for creature in self.creatures:
            if creature.isAlive:
                creature.draw(screen)

    def draw_food(self, screen):
        for food_item in self.food:
            food_item.draw(screen)
    
    def add_food(self):
        x = random.randint(405, 770)
        y = random.randint(30, 395)
        self.food.append(Food((255, 0, 0), (x, y), 5))

    def calculate_creature_fitness(self):
        for creature in self.creatures:
            if creature.isAlive:
                creature.timeSurvived = 30000
            creature.fitness = creature.timeSurvived + creature.foodEaten - creature.energySpent

        creature_fitness = sorted(self.creatures, key=lambda creature: creature.fitness)
        return creature_fitness
    
    def mutate_generation(self):
        creature_fitness = self.calculate_creature_fitness()
        newGenCreatures = []
        for creature in creature_fitness[-5:]:
            newGenCreatures.append(creature)
            for i in range(3):
                mutatedGenome = creature.genome.mutate()
                x = random.randint(400 + mutatedGenome.size, 775 - mutatedGenome.size)
                y = random.randint(25 + mutatedGenome.size, 400 - mutatedGenome.size)
                newGenCreatures.append(Creature(mutatedGenome, (0, 0, 255), (x, y), 100, True))
        
        return newGenCreatures
    
    def get_average_stats(self):
        totalSpeed = 0
        totalVision = 0
        totalEfficiency = 0
        totalSize = 0
        for creature in self.creatures:
            totalSpeed += creature.genome.speed
            totalVision += creature.genome.visionRadius
            totalEfficiency += creature.genome.energyEfficiency
            totalSize += creature.genome.size

        avgSpeed = totalSpeed / 20
        avgVision = totalVision / 20
        avgEfficiency = totalEfficiency / 20
        avgSize = totalSize / 20

        print("Speed:", avgSpeed)
        print("Vision:", avgVision)
        print("Efficiency:", avgEfficiency)
        print("Size:", avgSize)


