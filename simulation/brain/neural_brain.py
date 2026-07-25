from simulation.brain.base_brain import Brain
import numpy as np
import math

class NeuralBrain(Brain):
    def __init__(self, creature, weights):
        super().__init__(creature)

        # Define HyperParameters
        self.inputLayerSize = 5
        self.outputLayerSize = 2
        self.hiddenLayerSize = 6

        # Weights
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
        speed = float(abs(y2)) * self.creature.genome.speed

        # Convert heading into velocity components.
        vx = speed * math.sin(bearing)
        vy = -speed * math.cos(bearing)

        if not (math.isfinite(vx) and math.isfinite(vy)):
            return 0.0, 0.0

        return vx, vy
    
    def tanh(self, z):
        # Use NumPy's stable tanh implementation to avoid overflow/NaN values.
        return np.tanh(z)
    
    def getInputs(self, world):
        # Get nearest visible food coordinates.
        nearestFood = (world.left + world.width / 2, world.top + world.height / 2)
        nearestFoodDistance = math.inf

        for food_item in world.food:
            coordinates = food_item.position
            distance = self.getDistanceTo(coordinates)
            if distance <= self.creature.genome.visionRadius and distance < nearestFoodDistance:
                nearestFood = coordinates
                nearestFoodDistance = distance

        # Get nearest wall coordinates from the actual world rectangle.
        x, y = self.creature.position
        left = world.left
        right = world.left + world.width
        top = world.top
        bottom = world.top + world.height

        wallDistances = {
            'left': x - left,
            'right': right - x,
            'top': y - top,
            'bottom': bottom - y,
        }
        nearestWallName = min(wallDistances, key=wallDistances.get)
        nearestWallDistance = wallDistances[nearestWallName]

        if nearestWallName == 'left':
            x2, y2 = (left, y)
        elif nearestWallName == 'right':
            x2, y2 = (right, y)
        elif nearestWallName == 'top':
            x2, y2 = (x, top)
        else:
            x2, y2 = (x, bottom)

        x1, y1 = nearestFood
        dxFoodNormalised = (x1 - x) / self.creature.genome.visionRadius
        dyFoodNormalised = (y1 - y) / self.creature.genome.visionRadius

        dxWallNormalised = (x2 - x) / world.width
        dyWallNormalised = (y2 - y) / world.width

        return np.array([dxFoodNormalised, dyFoodNormalised, dxWallNormalised, dyWallNormalised, self.creature.energy / 100], dtype=float)
