# NeuroGenesis — An Artificial Evolution & Neuroevolution Simulator

*Watch intelligent behaviour emerge from nothing but selection, mutation, and time.*

<img width="400" height="400" alt="download" src="https://github.com/user-attachments/assets/3d6c87ba-c62d-4d5c-95b6-127a4c272f48" />


## Overview

NeuroGenesis is a from-scratch artificial life simulator built in Python. A
population of creatures with no programmed behaviour evolves, generation by
generation, to forage for food and avoid predators — using a genetic
algorithm I designed and implemented myself, alongside neural network
"brains" that are evolved rather than trained.

No pre-trained models, no LLM APIs, and no gradient descent are used
anywhere in this project. Every behaviour you see emerged purely from
selection and mutation acting on random initial populations.

**Core question this project investigates:** *Can intelligent behaviour
emerge purely from evolution, without backpropagation or hand-written
rules?*

<!-- INSERT: 2-3 sentence summary of your specific experimental findings,
     e.g. "After ~300 generations, average vision radius increased by X%
     and predator-evasion success rose from Y% to Z%." -->

---

## Demo

<!-- INSERT: primary demo video/GIF, e.g.
     [![Watch the demo](docs/media/thumbnail.png)](docs/media/demo.mp4)
-->

| Early generation | Late generation |
|---|---|
| <img width="200" height="200" alt="download (1)" src="https://github.com/user-attachments/assets/979f731c-0796-4c03-8f93-7887f44f732f" /> | <img width="200" height="200" alt="download (2)" src="https://github.com/user-attachments/assets/cbbd5235-be97-4c99-a126-0d9920c87a5a" /> |


<img width="117" height="161" alt="image" src="https://github.com/user-attachments/assets/e4c679c8-9e2f-4c1d-a3e5-68cbd75916c2" />

---

## Key Features

- **Custom genetic algorithm** — selection, crossover/mutation, and
  generational reproduction implemented from first principles (no
  off-the-shelf GA library).
- **Neuroevolution** — each creature is controlled by a small feedforward
  neural network whose *weights* are evolved rather than trained via
  backpropagation. Behaviour (foraging, obstacle avoidance, predator
  evasion) emerges entirely from selection pressure.
- **Evolving predator–prey dynamics** — predators and prey evolve
  concurrently, each with their own genome and fitness function, producing
  an evolutionary arms race between hunting and evasion strategies.
- **Configurable ecosystem** — population size, mutation rate, food
  density, network architecture, and predator count are all adjustable via
  a central configuration file, enabling repeatable experiments.
- **Data logging & visualisation** — per-generation statistics (average
  fitness, speed, vision, survival time, population size) are logged and
  plotted, so evolutionary trends are visible and measurable, not just
  anecdotal.
- **Modular architecture** — physical traits and neural "brains" are both
  encoded in a single `Genome`, and creature decision-making is built
  behind a swappable `Brain` interface, so new behaviours or agent types
  can be added without modifying existing simulation logic.

---

## How It Works

1. **Genome** — Each creature's entire blueprint (speed, vision radius,
   energy efficiency, and neural network weights) is encoded as a single
   genome.
2. **Brain** — On creation, a creature builds a small neural network from
   the weights stored in its genome. The network takes in sensory inputs
   (e.g. distance/angle to nearest food, nearest predator, and walls) and
   outputs movement decisions.
3. **Simulation** — Creatures live inside a bounded world, competing for
   food while avoiding predators, losing energy over time, and dying when
   energy runs out or they're caught.
4. **Fitness & selection** — At the end of each generation, creatures are
   scored on a fitness function (food eaten, time survived, distance
   explored, etc.). The fittest individuals reproduce.
5. **Mutation** — Offspring inherit their parents' genome with small
   random mutations, allowing both physical traits and brain weights to
   drift and improve over generations.
6. **Repeat** — Over hundreds of generations, this loop produces
   increasingly capable creatures with no explicit programming of *how*
   to forage or evade — only *what counts as success*.

<!-- INSERT: architecture diagram if you have one, e.g.
     ![Architecture diagram](docs/media/architecture.png) -->

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python | Core language |
| Pygame | Simulation rendering and game loop |
| NumPy | Neural network forward propagation, vector maths |
| Pytest | Unit tests for genome mutation and fitness logic |

---

## Getting Started

### Prerequisites
- Python 3.x
- pip

### Configuration
All simulation parameters (population size, mutation rate, food density,
network size, predator count) can be adjusted in `config.py` without
touching any simulation code, allowing quick experimentation.

---

## Project Structure
```
NeuroGenesis/
├── main.py
├── config.py
├── simulation/
│   ├── world.py
│   ├── creature.py
│   ├── predator.py
│   ├── food.py
│   ├── genome.py
│   ├── brain/
│   │   ├── base_brain.py
│   │   ├── rule_based_brain.py
│   │   └── neural_brain.py
│   └── evolution.py
├── analysis/
│   ├── logger.py
│   └── plots.py
├── tests/
└── data/
```

---

## What I Learned

 - Trade-offs in designing a fitness function (by increasing the rewards for survival time, food eaten, etc., I saw different behaviours evolving as a result).
 - Creatures' movement often became static; I discovered that this odd behaviour was due to the calculation of the inputs, as they were not relative to the creature itself.
 - I decided on the mutation rate after constant iterations, testing to see what worked and what didn't.

<!-- INSERT: 3-5 sentences in your own words — this is what interviewers
     actually read. Suggested angles:
     - trade-offs in designing a fitness function
     - why you separated physical genes from brain weights but stored
       them in one genome
     - a bug or unexpected emergent behaviour and how you diagnosed it
     - how you decided on network architecture / mutation rate
-->

## Future Work

- Dynamic network topology evolution (NEAT-style), rather than a fixed
  network shape.
- Sexual reproduction / crossover between two parent genomes.
- Multiple co-evolving species occupying different ecological niches.
- Seasonal/weather effects on food availability.

---

## Author

Freddy Stokes

