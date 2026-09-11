import pygame
from simulation.food import Food
from simulation.creature import Creature
from simulation.predator import Predator
import random
import numpy as np

class World:
    def __init__(self, left, top, width, height, colour, food, creatures, predators):
        self.left = left
        self.top = top
        self.width = width
        self.height = height
        self.colour = colour
        self.food = food
        self.creatures = creatures
        self.predators = predators
    
    def draw_world(self, screen):
        pygame.draw.rect(screen, self.colour, pygame.Rect(self.left, self.top, self.width, self.height))
    
    def draw_creatures(self, screen):
        for creature in self.creatures:
            if creature.isAlive:
                creature.draw(screen)

    def draw_predators(self, screen):
            for predator in self.predators:
                if predator.isAlive:
                    predator.draw(screen)

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
                creature.timeSurvived = 20000
            creature.fitness = (creature.timeSurvived / 500) + (2 * creature.foodEaten) 

        creature_fitness = sorted(self.creatures, key=lambda creature: creature.fitness)
        return creature_fitness

    def calculate_predator_fitness(self):
        for predator in self.predators:
            if predator.isAlive:
                predator.timeSurvived = 20000
            predator.fitness = (predator.timeSurvived / 1000) + (2 * predator.foodEaten)

        predator_fitness = sorted(self.predators, key=lambda predator: predator.fitness)
        return predator_fitness
    
    def mutate_generation(self):
        creature_fitness = self.calculate_creature_fitness()
        newGenCreatures = []
        for creature in creature_fitness[-3:]:
            newGenCreatures.append(creature)
            for i in range(9):
                mutatedGenome = creature.genome.mutate()
                x = random.randint(400 + mutatedGenome.size, 775 - mutatedGenome.size)
                y = random.randint(25 + mutatedGenome.size, 400 - mutatedGenome.size)
                newGenCreatures.append(Creature(mutatedGenome, (0, 0, 255), (x, y), 100, True))

        predator_fitness = self.calculate_predator_fitness()
        newGenPredators = []
        for predator in predator_fitness[-2:]:
            newGenPredators.append(predator)
            for i in range(4):
                mutatedGenome = predator.genome.mutate()
                x = random.randint(400 + mutatedGenome.size, 775 - mutatedGenome.size)
                y = random.randint(25 + mutatedGenome.size, 400 - mutatedGenome.size)
                newGenPredators.append(Predator(mutatedGenome, (127.5, 0, 127.5), (x, y), 100, True))

        return newGenCreatures, newGenPredators
    
    def get_average_stats(self):
        totalSpeed = 0
        totalVision = 0
        totalEfficiency = 0
        totalSize = 0
        totalWeights = np.zeros(60)
        n = len(self.creatures)
        for creature in self.creatures:
            totalSpeed += creature.genome.speed
            totalVision += creature.genome.visionRadius
            totalEfficiency += creature.genome.energyEfficiency
            totalSize += creature.genome.size
            for i in range(len(creature.genome.weights)):
                totalWeights[i] += creature.genome.weights[i]


        avgSpeed = totalSpeed / n
        avgVision = totalVision / n
        avgEfficiency = totalEfficiency / n
        avgSize = totalSize / n
        for total in totalWeights:
            total /= n
        avgWeights = totalWeights

        print("Speed:", avgSpeed)
        print("Vision:", avgVision)
        print("Efficiency:", avgEfficiency)
        print("Size:", avgSize)
        print("Average weights:", avgWeights)


