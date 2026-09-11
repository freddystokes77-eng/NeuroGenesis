from simulation.creature import Creature
from simulation.brain.neural_predator_brain import NeuralPredatorBrain
import math

class Predator(Creature):
    def __init__(self, genome, colour, position, energy, isAlive):
        super().__init__(genome, colour, position, energy, isAlive)
        self.brain = NeuralPredatorBrain(self, genome.weights)
    
    def checkForCollision(self, world):
        x1, y1 = self.position
        for creature in world.creatures:
            x2, y2 = creature.position
            distance = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            if distance < self.genome.size + creature.genome.size:
                world.creatures.remove(creature)
                creature.isAlive = False
                self.gain_energy()