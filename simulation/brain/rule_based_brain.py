from simulation.brain.base_brain import Brain

class RuleBasedBrain(Brain):
    def decideDirection(self, world):
        for food_item in world.food:
            coordinates = food_item.position
            distance = self.getDistanceTo(coordinates)
            if distance <= self.creature.genome.visionRadius:
                speed_x, speed_y = self.getSpeed(coordinates)
                return speed_x, speed_y
        return self.creature.speed_x, self.creature.speed_y