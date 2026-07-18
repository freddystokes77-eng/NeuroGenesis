import pygame
from simulation.food import Food
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
        self.food.append(Food((255, 0, 0), (random.randint(self.left + 10, self.left + self.width - 10), random.randint(self.top + 10, self.top + self.height - 10)), 5))

        
