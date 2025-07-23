#!/usr/bin/env python3
"""
PyEvolve Demo - A Self-Contained Genetic Algorithm Simulation

This demo simulates the evolution of creatures with four traits:
- Speed, Strength, Vision, and Stamina

The simulation runs for multiple generations, selecting the fittest creatures
to produce offspring with mutation, and visualizes the evolutionary progress.

Dependencies: matplotlib, numpy (install with: pip install matplotlib numpy)
"""

import random
import matplotlib.pyplot as plt
import os


class Creature:
    """Represents a creature with four traits and calculates its fitness."""

    def __init__(self, speed, strength, vision, stamina):
        self.speed = speed
        self.strength = strength
        self.vision = vision
        self.stamina = stamina
        self.fitness = self.calculate_fitness()

    def __repr__(self):
        return f"<Creature speed={self.speed}, strength={self.strength}, vision={self.vision}, stamina={self.stamina}, fitness={self.fitness:.2f}>"

    def calculate_fitness(self):
        """Calculate fitness as a weighted sum of all traits."""
        fitness = (0.3 * self.speed) + (0.3 * self.strength) + (0.2 * self.vision) + (0.2 * self.stamina)
        return fitness


def calculate_offspring(parent1, parent2):
    """Create offspring from two parent creatures with potential mutation."""
    # Average the traits from both parents
    speed = (parent1.speed + parent2.speed) / 2
    strength = (parent1.strength + parent2.strength) / 2
    vision = (parent1.vision + parent2.vision) / 2
    stamina = (parent1.stamina + parent2.stamina) / 2

    # Apply mutation with 10% chance
    if random.random() < 0.1:
        speed += random.randint(-5, 5)
        strength += random.randint(-5, 5)
        vision += random.randint(-5, 5)
        stamina += random.randint(-5, 5)

    # Ensure traits stay within valid bounds (1-100)
    speed = max(1, min(100, int(speed)))
    strength = max(1, min(100, int(strength)))
    vision = max(1, min(100, int(vision)))
    stamina = max(1, min(100, int(stamina)))

    return Creature(speed, strength, vision, stamina)


def produce_next_generation(survivors, population_count):
    """Generate the next generation of creatures from the given survivors."""
    next_generation = []
    for _ in range(population_count):
        parent1 = random.choice(survivors)
        parent2 = random.choice(survivors)
        offspring = calculate_offspring(parent1, parent2)
        next_generation.append(offspring)
    return next_generation


def run_evolution_simulation(population_count=100, generation_goal=10, survival_rate=0.2):
    """
    Run the complete evolution simulation.

    Args:
        population_count (int): Number of creatures in each generation
        generation_goal (int): Number of generations to simulate
        survival_rate (float): Fraction of population that survives to reproduce

    Returns:
        list: All generations of creatures
    """
    print(f"Starting evolution simulation with {population_count} creatures for {generation_goal} generations")
    print(f"Survival rate: {survival_rate * 100}% per generation\n")

    # Initialize first generation with random traits
    population = []
    for i in range(population_count):
        speed = random.randint(1, 100)
        strength = random.randint(1, 100)
        vision = random.randint(1, 100)
        stamina = random.randint(1, 100)
        creature = Creature(speed, strength, vision, stamina)
        population.append(creature)

    # Sort by fitness (highest first)
    population = sorted(population, key=lambda c: c.fitness, reverse=True)
    generations = [population]

    # Evolve through generations
    survivors_count = int(population_count * survival_rate)

    for gen in range(1, generation_goal + 1):
        survivors = generations[-1][:survivors_count]  # Top performers survive
        next_generation = produce_next_generation(survivors, population_count)
        next_generation = sorted(next_generation, key=lambda c: c.fitness, reverse=True)
        generations.append(next_generation)

    # Print generation statistics
    for i, gen in enumerate(generations):
        avg_fitness = sum(c.fitness for c in gen) / len(gen)
        max_fitness = max(c.fitness for c in gen)
        min_fitness = min(c.fitness for c in gen)
        print(f"Generation {i}: Avg Fitness={avg_fitness:.2f}, Max Fitness={max_fitness:.2f}, Min Fitness={min_fitness:.2f}")

    return generations


def create_visualizations(generations, output_dir="graphs"):
    """Create and save visualization charts for the evolution simulation."""

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Calculate stats per generation
    avg_fitnesses = [sum(c.fitness for c in gen) / len(gen) for gen in generations]
    max_fitnesses = [max(c.fitness for c in gen) for gen in generations]
    min_fitnesses = [min(c.fitness for c in gen) for gen in generations]
    gen_nums = list(range(len(generations)))

    # Identify the peak generation by average fitness
    best_gen_idx = avg_fitnesses.index(max(avg_fitnesses))

    # --- Fitness Trends Over Generations ---
    plt.figure(figsize=(12, 6))
    plt.plot(gen_nums, avg_fitnesses, label='Average Fitness', linewidth=2)
    plt.plot(gen_nums, max_fitnesses, label='Max Fitness', linestyle='--', alpha=0.7)
    plt.plot(gen_nums, min_fitnesses, label='Min Fitness', linestyle='--', alpha=0.7)
    plt.axvline(x=best_gen_idx, color='gold', linestyle=':', linewidth=2, label=f'Best Gen: {best_gen_idx}')
    plt.title("Fitness Over Generations", fontsize=14)
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "fitness_trends.png"))
    plt.show()

    # --- Attribute Distribution (Last Generation Histogram) ---
    last_gen = generations[-1]
    plt.figure(figsize=(12, 6))
    plt.hist([c.speed for c in last_gen], bins=15, alpha=0.6, label='Speed')
    plt.hist([c.strength for c in last_gen], bins=15, alpha=0.6, label='Strength')
    plt.hist([c.vision for c in last_gen], bins=15, alpha=0.6, label='Vision')
    plt.hist([c.stamina for c in last_gen], bins=15, alpha=0.6, label='Stamina')
    plt.title("Trait Distribution - Last Generation", fontsize=14)
    plt.xlabel("Attribute Value")
    plt.ylabel("Creature Count")
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "last_gen_distribution.png"))
    plt.show()

    # --- Trait Evolution Over Time ---
    avg_speed = [sum(c.speed for c in gen)/len(gen) for gen in generations]
    avg_strength = [sum(c.strength for c in gen)/len(gen) for gen in generations]
    avg_vision = [sum(c.vision for c in gen)/len(gen) for gen in generations]
    avg_stamina = [sum(c.stamina for c in gen)/len(gen) for gen in generations]

    plt.figure(figsize=(12, 6))
    plt.plot(gen_nums, avg_speed, label='Speed', linewidth=2)
    plt.plot(gen_nums, avg_strength, label='Strength', linewidth=2)
    plt.plot(gen_nums, avg_vision, label='Vision', linewidth=2)
    plt.plot(gen_nums, avg_stamina, label='Stamina', linewidth=2)
    plt.title("Average Trait Values Over Generations", fontsize=14)
    plt.xlabel("Generation")
    plt.ylabel("Trait Value")
    plt.ylim(0, 100)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()
    plt.savefig(os.path.join(output_dir, "trait_trends.png"))
    plt.show()

    print(f"\nVisualization charts saved to '{output_dir}' directory")


def main():
    """Main function to run the complete evolution demo."""
    print("=" * 60)
    print("            PyEvolve - Genetic Algorithm Demo")
    print("=" * 60)

    # Configuration
    population_count = 100
    generation_goal = 10
    survival_rate = 0.2  # Top 20% survive

    # Run the simulation
    generations = run_evolution_simulation(
        population_count=population_count,
        generation_goal=generation_goal,
        survival_rate=survival_rate
    )

    # Create visualizations
    print("\nGenerating visualizations...")
    create_visualizations(generations)

    # Show some final statistics
    print("\n" + "=" * 60)
    print("                    FINAL RESULTS")
    print("=" * 60)

    first_gen = generations[0]
    last_gen = generations[-1]

    print(f"Initial Generation Avg Fitness: {sum(c.fitness for c in first_gen) / len(first_gen):.2f}")
    print(f"Final Generation Avg Fitness: {sum(c.fitness for c in last_gen) / len(last_gen):.2f}")

    print(f"\nBest creature in final generation:")
    best_creature = max(last_gen, key=lambda c: c.fitness)
    print(f"  {best_creature}")

    print(f"\nWorst creature in final generation:")
    worst_creature = min(last_gen, key=lambda c: c.fitness)
    print(f"  {worst_creature}")

    fitness_improvement = (sum(c.fitness for c in last_gen) / len(last_gen)) - (sum(c.fitness for c in first_gen) / len(first_gen))
    print(f"\nOverall fitness improvement: {fitness_improvement:+.2f}")


if __name__ == "__main__":
    # Set random seed for reproducible results (optional)
    # random.seed(42)

    main()
