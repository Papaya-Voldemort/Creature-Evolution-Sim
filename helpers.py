import random

class Creature:
    def __init__(self, speed, strength, vision, stamina):
        self.speed = speed
        self.strength = strength
        self.vision = vision
        self.stamina = stamina
        self.fitness = self.calculate_fitness()

    def __repr__(self):
        return f"<Creature speed={self.speed}, strength={self.strength}, vision={self.vision}, stamina={self.stamina}, fitness={self.fitness:.2f}>"

    def calculate_fitness(self):
        fitness = (0.3 * self.speed) + (0.3 * self.strength) + (0.2 * self.vision) + (0.2 * self.stamina)
        return fitness


def calculate_offspring(parent1, parent2):
    speed = (parent1.speed + parent2.speed) / 2
    strength = (parent1.strength + parent2.strength) / 2
    vision = (parent1.vision + parent2.vision) / 2
    stamina = (parent1.stamina + parent2.stamina) / 2

    if random.random() < 0.1:  # 10% mutation chance
        speed += random.randint(-5, 5)
        strength += random.randint(-5, 5)
        vision += random.randint(-5, 5)
        stamina += random.randint(-5, 5)

    speed = max(1, min(100, int(speed)))
    strength = max(1, min(100, int(strength)))
    vision = max(1, min(100, int(vision)))
    stamina = max(1, min(100, int(stamina)))

    return Creature(speed, strength, vision, stamina)

def produce_next_generation(survivors, population_count):
    """
    Generate the next generation of creatures from the given survivors.
    Args:
        survivors (list of Creature): The selected top-performing creatures.
        population_count (int): The number of offspring to produce.
    Returns:
        list of Creature: The next generation population.
    """
    next_generation = []
    for _ in range(population_count):
        parent1 = random.choice(survivors)
        parent2 = random.choice(survivors)
        offspring = calculate_offspring(parent1, parent2)
        next_generation.append(offspring)
    return next_generation
