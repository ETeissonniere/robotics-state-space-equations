# Spring-Mass-Damper System Simulation

Implementation of the state space equations for a spring + mass damper system. This simulation models a mass attached to a spring with damping, subject to external forces.


This projects uses [`uv`](https://github.com/astral-sh/uv) for easier dependency management, you may run it via `uv run main.py`.

## Command Line Arguments

All system parameters can be configured via command line arguments:

- `-m`, `--mass`: Mass of the object (kg) [default: 1.0]
- `-k`, `--spring_constant`: Spring constant (N/m) [default: 10.0]
- `-c`, `--damping`: Damping coefficient (Ns/m) [default: 0.5]
- `-u`, `--force`: External force (N) [default: 0.0]
- `-x0`, `--initial_position`: Initial position (m) [default: 1.0]
- `-v0`, `--initial_velocity`: Initial velocity (m/s) [default: 0.0]
- `-t`, `--simulation_time`: Simulation time (s) [default: 10.0]

Example with custom parameters:
```bash
uv run main.py --mass 2.0 --spring_constant 15.0 --damping 0.8 --force 1.0
```

## Output

The simulation generates a plot showing:
1. Position vs. time
2. Velocity vs. time

