import pygame
import random
import math

class Creature:
    def __init__(self, colour, position, radius, speed, energy, isAlive):
        self.colour = colour
        self.position = position
        self.radius = radius
        self.speed = speed
        self.speed_x = random.randint(-speed, speed)
        self.speed_y = random.randint(-speed, speed)
        self.energy = energy
        self.isAlive = isAlive

    def draw(self, screen):
        pygame.draw.circle(screen, self.colour, self.position, self.radius)

    def drain_energy(self):
        self.energy -= 0.1
        if self.energy <= 0:
            self.isAlive = False
        else:
            print("Creature energy: ", self.energy)

    def gain_energy(self):
        self.energy += 10
        print("Food eaten!")

    def move(self, world):
        x, y = self.position
        
        # Update postion
        x += self.speed_x
        y += self.speed_y


        # Bounce off screen edges
        if x - self.radius <= world.left or x + self.radius >= world.left + world.width:
            self.speed_x *= -1
        if y - self.radius <= world.top or y + self.radius >= world.top + world.height:
            self.speed_y *= -1

        self.position = x, y
        self.checkForCollision(world)
    
    def checkForCollision(self, world):
        x1, y1 = self.position
        for food_item in world.food:
            x2, y2 = food_item.position
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if distance < self.radius + food_item.radius:
                print("Collision detected")
                world.food.remove(food_item)
                del food_item
                world.add_food()
                self.gain_energy()
                
