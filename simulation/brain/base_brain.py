import math
from abc import ABC, abstractmethod
class Brain(ABC):
    def __init__(self, creature):
        self.creature = creature
    
    @abstractmethod
    def decideDirection(self, world):
        pass
    
    def getDistanceTo(self, coordinates):
        x1, y1 = self.creature.position
        x2, y2 = coordinates
        distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
        return distance
    
    def getSpeed(self, coordinates):
        x1, y1 = self.creature.position
        x2, y2 = coordinates
        dx = x2 - x1
        dy = y2 - y1
        distance = math.sqrt(dx**2 + dy**2)
        unit_x = dx / distance
        unit_y = dy / distance
        speed_x = unit_x * self.creature.genome.speed
        speed_y = unit_y * self.creature.genome.speed
        return speed_x, speed_y