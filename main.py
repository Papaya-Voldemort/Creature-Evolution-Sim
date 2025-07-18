import random
from helpers import Creature
from helpers import calculate_offspring, produce_next_generation
import matplotlib.pyplot as plt
import os

population_count = 100
population = []
generation_goal = 10

generations = []

for i in range(population_count):
    speed = random.randint(1, 100)
    strength = random.randint(1, 100)
    vision = random.randint(1, 100)
    stamina = random.randint(1, 100)
    creature = Creature(speed, strength, vision, stamina)
    population.append(creature)

population = sorted(population, key=lambda c: c.fitness, reverse=True)
generations.append(population)

for gen in range(1, generation_goal + 1):
    survivors = generations[-1][:20]  # top 20 from previous generation
    next_generation = produce_next_generation(survivors, population_count)
    next_generation = sorted(next_generation, key=lambda c: c.fitness, reverse=True)
    generations.append(next_generation)

for i, gen in enumerate(generations):
    avg_fitness = sum(c.fitness for c in gen) / len(gen)
    max_fitness = max(c.fitness for c in gen)
    min_fitness = min(c.fitness for c in gen)
    print(f"Generation {i}: Avg Fitness={avg_fitness:.2f}, Max Fitness={max_fitness:.2f}, Min Fitness={min_fitness:.2f}")

# Enhanced Analytics & Visualization Section

# Ensure output directory exists
output_dir = "graphs"
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
