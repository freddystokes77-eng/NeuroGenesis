from dataclasses import dataclass
import random
from simulation.creature import Creature

@dataclass
class Genome:
    speed : float
    visionRadius : float
    energyEfficiency : float
    size : int
    weights : list[float]

    def mutate(self):
        # mutatedSpeed = random.uniform(self.speed - 0.05 * self.speed, self.speed + 0.05 * self.speed)
        # mutatedVision = random.uniform(self.visionRadius - 0.05 * self.visionRadius, self.visionRadius + 0.05 * self.visionRadius)
        # mutatedEfficiency = random.uniform(self.energyEfficiency - 0.05 * self.energyEfficiency, self.energyEfficiency + 0.05 * self.energyEfficiency)
        # mutatedSize = random.randint(self.size - 1, self.size + 1)
        mutatedSpeed = self.speed
        mutatedVision = self.visionRadius
        mutatedEfficiency = self.energyEfficiency
        mutatedSize = self.size
        mutation_rate = 0.10
        mutation_amount = 0.05

        # Make a copy so the original genome isn't changed
        mutatedWeights = self.weights.copy()

        for i in range(len(mutatedWeights)):
            if random.random() < mutation_rate:
                mutatedWeights[i] += random.uniform(
                    -mutation_amount,
                    mutation_amount
                )

        if type(self) == Creature:
            if mutatedSpeed < 0.2:
                mutatedSpeed = 0.2
            elif mutatedSpeed > 1:
                mutatedSpeed = 1
            elif mutatedVision < 50:
                mutatedVision = 50
            elif mutatedVision > 100:
                mutatedVision = 100
            elif mutatedSize < 3:
                mutatedSize = 3
            elif mutatedSize > 5:
                mutatedSize = 5
        else:
            if mutatedSpeed < 0.5:
                mutatedSpeed = 0.5
            elif mutatedSpeed > 1.5:
                mutatedSpeed = 1.5
            elif mutatedVision < 50:
                mutatedVision = 50
            elif mutatedVision > 100:
                mutatedVision = 100
            elif mutatedSize < 5:
                mutatedSize = 5
            elif mutatedSize > 8:
                mutatedSize = 8
    
        if mutatedEfficiency < 20:
            mutatedEfficiency = 20
        elif mutatedEfficiency > 80:
            mutatedEfficiency = 80

        
        return Genome(mutatedSpeed, mutatedVision, mutatedEfficiency, mutatedSize, mutatedWeights)