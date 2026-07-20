from dataclasses import dataclass
import random

@dataclass
class Genome:
    speed : float
    visionRadius : float
    energyEfficiency : float
    size : int

    def mutate(self):
        mutatedSpeed = random.uniform(self.speed - 0.1 * self.speed, self.speed + 0.1 * self.speed)
        mutatedVision = random.uniform(self.visionRadius - 0.1 * self.visionRadius, self.visionRadius + 0.1 * self.visionRadius)
        mutatedEfficiency = random.uniform(self.energyEfficiency - 0.1 * self.energyEfficiency, self.energyEfficiency + 0.1 * self.energyEfficiency)
        mutatedSize = random.randint(self.size - 1, self.size + 1)

        if mutatedSpeed < 0.5:
            mutatedSpeed = 0.5
        elif mutatedSpeed > 2:
            mutatedSpeed = 2
        
        if mutatedVision < 25:
            mutatedVision = 25
        elif mutatedVision > 50:
            mutatedVision = 50
        
        if mutatedEfficiency < 20:
            mutatedEfficiency = 20
        elif mutatedEfficiency > 80:
            mutatedEfficiency = 80
        
        if mutatedSize < 1:
            mutatedSize = 1
        elif mutatedSize > 10:
            mutatedSize = 10
        
        return Genome(mutatedSpeed, mutatedVision, mutatedEfficiency, mutatedSize)