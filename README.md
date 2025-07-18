# PyEvolve: Genetic Algorithm Simulation

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.6%2B-brightgreen)

> **Summer of Making 2025 Project**

PyEvolve is a simple yet powerful genetic algorithm simulation that demonstrates evolutionary principles through computational modeling. The simulation creates a population of virtual creatures with various attributes (speed, strength, vision, and stamina), evolves them over multiple generations, and visualizes the results.

## 🧬 Features

- **Creature Simulation**: Create and evolve populations of virtual creatures with unique attributes
- **Natural Selection**: Implements fitness-based selection to simulate evolutionary pressure
- **Genetic Inheritance**: Offspring inherit traits from parents with random mutations
- **Data Visualization**: Generate graphs showing fitness trends and trait evolution over generations
- **Customizable Parameters**: Easily modify population size, generation count, and selection criteria

## 📊 Visualizations

PyEvolve generates several visualizations to help understand the evolutionary process:

- **Fitness Trends**: Track average, maximum, and minimum fitness across generations
- **Trait Evolution**: See how average trait values change over time
- **Trait Distribution**: Analyze the distribution of traits in the final generation

*Note: GPT-4.1 was used to help design and optimize the visualization components of this project.*

## 🚀 Quick Start

### Installation

```bash
# Clone the repository
git clone https://github.com/Papaya-Voldemort/Creature-Evolution-Sim.git
cd Creature-Evolution-Sim

# Install dependencies
pip install -r requirements.txt
```

### Running the Simulation

```bash
python main.py
```

This will:
1. Create an initial population of 100 creatures with random attributes
2. Evolve the population over 10 generations
3. Display statistics for each generation
4. Generate visualization graphs in the `graphs/` directory

## 🔧 Customization

You can easily modify the simulation parameters in `main.py`:

```python
# Change these values to customize your simulation
population_count = 100  # Number of creatures in each generation
generation_goal = 10    # Number of generations to simulate
```

Other customization options:
- Modify the selection criteria (currently takes top 20 creatures)
- Edit the `calculate_fitness` method to change how fitness is determined
- Adjust mutation rates in the `calculate_offspring` function

## 🧪 How It Works

1. **Initialization**: Creates a population of creatures with random attributes
2. **Fitness Calculation**: Each creature's fitness is calculated based on its attributes
3. **Selection**: The fittest creatures are selected to reproduce
4. **Reproduction**: New creatures are created by combining traits from parents
5. **Mutation**: Random mutations are introduced to maintain genetic diversity
6. **Repeat**: Steps 2-5 are repeated for multiple generations

## 📋 Future Development

I plan to add more after the Summer of Making 2025, including:
- More complex traits and behaviors for creatures
- Interactive visualization tools
- User-defined fitness functions
- And possibly a GUI for easier interaction

## 🤝 Contributing

Contributions are welcome! Feel free to submit pull requests or open issues to suggest improvements.

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

*Created for Summer of Making 2025*