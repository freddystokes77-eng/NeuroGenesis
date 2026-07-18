import pygame

class Food:
    def __init__(self, colour, position, radius):
        self.colour = colour
        self.position = position
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)