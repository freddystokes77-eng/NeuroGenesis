from simulation.brain.base_brain import Brain
import numpy as np
import math

class NeuralPredatorBrain(Brain):
    def __init__(self, creature, weights):
        super().__init__(creature)

        # Define HyperParameters
        self.inputLayerSize = 5
        self.outputLayerSize = 2
        self.hiddenLayerSize = 6

        # Define weights
        self.W1 = np.array([weights[:6], weights[6:12], weights[12:18], weights[18:24], weights[24:30]])
        self.W2 = np.array([weights[30:32], weights[32:34], weights[34:36], weights[36:38], weights[38:40], weights[40:42]])
        
    def decide(self, world):
        X = self.getInputs(world)
        # Propagate inputs through network
        self.z2 = np.dot(X, self.W1)
        self.a2 = self.tanh(self.z2)
        self.z3 = np.dot(self.a2, self.W2)
        y1, y2 = self.tanh(self.z3)

        bearing = float(y1) * math.pi
        speed = 0.2 * self.creature.genome.speed + 0.8 * (float(abs(y2)) * self.creature.genome.speed)

        # Convert heading into velocity components.
        vx = speed * math.sin(bearing)
        vy = -speed * math.cos(bearing)

        if not (math.isfinite(vx) and math.isfinite(vy)):
            return 0.0, 0.0

        return vx, vy, bearing
    
    def tanh(self, z):
        # Use NumPy's stable tanh implementation to avoid overflow/NaN values.
        return np.tanh(z)
    
    def getInputs(self, world):
        # Get nearest visible creature coordinates.
        nearestCreature = (world.left + world.width / 2, world.top + world.height / 2)
        nearestCreatureDistance = math.inf
        isCreatureVisible = False

        for creature in world.creatures:
            coordinates = creature.position
            distance = self.getDistanceTo(coordinates)
            if distance <= self.creature.genome.visionRadius and distance < nearestCreatureDistance:
                nearestCreature = coordinates
                nearestCreatureDistance = distance
                isCreatureVisible = True

        # Get nearest wall coordinates from the actual world rectangle.
        x, y = self.creature.position
        left = world.left
        right = world.left + world.width
        top = world.top
        bottom = world.top + world.height
        worldDiagonal = math.sqrt(world.width**2 + world.height**2)

        tList = []
        dir_x = math.sin(self.creature.heading)
        dir_y = -math.cos(self.creature.heading)

        if dir_x != 0:
            tList.append((left - x) / dir_x)
            tList.append((right - x) / dir_x)
        if dir_y != 0:
            tList.append((top - y) / dir_y)
            tList.append((bottom - y) / dir_y)

        smallestPositiveT = min([x for x in tList if x >= 0])
        normalisedDistanceToWallAhead = smallestPositiveT / worldDiagonal

        x1, y1 = nearestCreature
        normalisedCreatureDirection = math.atan2(x1 - x, -(y1 - y)) - self.creature.heading
        normalisedCreatureDirection = (normalisedCreatureDirection) % (2 * math.pi) - math.pi
        normalisedCreatureDirection /= math.pi
        normalisedCreatureDistance = nearestCreatureDistance / worldDiagonal


        return np.array([int(isCreatureVisible), normalisedCreatureDirection, normalisedCreatureDistance, normalisedDistanceToWallAhead ,self.creature.energy / 200], dtype=float)
