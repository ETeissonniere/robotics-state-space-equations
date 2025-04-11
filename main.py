# Spring mass system
#
# The state is represented as:
# - x_1: position along the x axis
# - x_2: velocity along the x axis
#
# As per newton's second law of motion, F = m * a.
# Couple forces are applied to the system:
# - Spring force: F_spring = -k * x_1
# - Damping force: F_damping = -c * x_2
# - External force: F_external = u
#
# So:
# m * x_2' = F_spring + F_damping + F_external
# m * x_2' = -k * x_1 - c * x_2 + u
# x_2' = (-k * x_1 - c * x_2 + u) / m
#
# Thus, this gives us:
# - x_1' = x_2
# - x_2' = (-k * x_1 - c * x_2 + u) / m
#
# Converting to state space, we get: 
# x = [x_1 x_2]
# x' = [x_1'] = A * x + B * u = [0       1] * x + [0  ] * u
#      [x_2']                   [-k/m -c/m]       [1/m]
#
# Since we only care about position, we can set y as:
# y = [x_1] = C * x + D * u = [1 0] * x + [0] * u

# Spring mass system simulation
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import argparse

def spring_mass_system(t, state, k, m, c, u):
    """
    State space representation of spring-mass system
    state[0] = x_1 (position)
    state[1] = x_2 (velocity)
    """
    x1, x2 = state
    
    # State equations:
    # x1' = x2
    # x2' = (-k * x1 - c * x2 + u) / m
    dx1_dt = x2
    dx2_dt = (-k * x1 - c * x2 + u) / m
    
    return [dx1_dt, dx2_dt]

def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description='Spring-Mass System Simulation')
    parser.add_argument('--mass', '-m', type=float, default=1.0,
                      help='Mass of the object (kg)')
    parser.add_argument('--spring_constant', '-k', type=float, default=10.0,
                      help='Spring constant (N/m)')
    parser.add_argument('--damping', '-c', type=float, default=0.5,
                      help='Damping coefficient (Ns/m)')
    parser.add_argument('--force', '-u', type=float, default=0.0,
                      help='External force (N)')
    parser.add_argument('--initial_position', '-x0', type=float, default=1.0,
                      help='Initial position (m)')
    parser.add_argument('--initial_velocity', '-v0', type=float, default=0.0,
                      help='Initial velocity (m/s)')
    parser.add_argument('--simulation_time', '-t', type=float, default=10.0,
                      help='Simulation time (s)')
    
    args = parser.parse_args()
    
    # Initial conditions
    initial_state = [args.initial_position, args.initial_velocity]
    
    # Time points
    t_span = (0, args.simulation_time)
    t_eval = np.linspace(0, args.simulation_time, 1000)
    
    # Solve the differential equations
    solution = solve_ivp(
        spring_mass_system, 
        t_span,
        initial_state,
        t_eval=t_eval,
        args=(args.spring_constant, args.mass, args.damping, args.force),
        method='RK45'
    )
    
    # Plot results
    plt.figure(figsize=(12, 8))
    
    # Position vs time
    plt.subplot(2, 1, 1)
    plt.plot(solution.t, solution.y[0], 'b-', label='Position')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Position (m)')
    plt.title('Spring-Mass System Response')
    plt.legend()
    
    # Velocity vs time
    plt.subplot(2, 1, 2)
    plt.plot(solution.t, solution.y[1], 'r-', label='Velocity')
    plt.grid(True)
    plt.xlabel('Time (s)')
    plt.ylabel('Velocity (m/s)')
    plt.legend()
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main()

