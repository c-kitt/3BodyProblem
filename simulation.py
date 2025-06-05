import random
import matplotlib.pyplot as plt
import visualization

# Constants 
G = 15000.0 # Impact of gravity
MASS = 1.0
dt = 0.03 # Speed of sim
num_steps = 10000 # Length of simulation
SOFTENING = 8.0 # This accounts for 1/r^2 as bodies move closer


# Initialize positions and velocities
positions = [
    [random.uniform(0, 50), random.uniform(0, 50)],
    [random.uniform(0, 0), random.uniform(0, 0)],
    [random.uniform(0, -50), random.uniform(0, -50)],
]
velocities = [
    [random.uniform(-5, 5), random.uniform(-5, 5)],
    [random.uniform(-5, 5), random.uniform(-5, 5)],
    [random.uniform(-5, 5), random.uniform(-5, 5)],
]

def compute_force(pos_i, pos_j):
    dx = pos_j[0] - pos_i[0]
    dy = pos_j[1] - pos_i[1]
    r_squared = dx**2 + dy**2 + SOFTENING**2 # Softening reduces impact of r^2 when distance between bodies is ~0
    r = r_squared ** 0.5
    if r == 0:
        return [0.0, 0.0]
    F = (G * MASS * MASS) / r_squared # F between two bodies
    Fx = F * (dx / r) 
    Fy = F * (dy / r)
    return [Fx, Fy]


plt.ion()  

for step in range(num_steps): # Primary loop
    # Reset net forces
    net_forces = [
        [0.0, 0.0],
        [0.0, 0.0],
        [0.0, 0.0],
    ]
    # Calculate net force on each body
    for i in range(3): 
        for j in range(3):
            if i != j:
                force = compute_force(positions[i], positions[j])
                net_forces[i][0] += force[0] # Fx, total
                net_forces[i][1] += force[1] # Fy, total
    # Accelerations for each body
    accelerations = [
        [net_forces[0][0] / MASS, net_forces[0][1] / MASS],
        [net_forces[1][0] / MASS, net_forces[1][1] / MASS],
        [net_forces[2][0] / MASS, net_forces[2][1] / MASS],
    ]
    # Update velocities
    for i in range(3):
        velocities[i][0] += accelerations[i][0] * dt
        velocities[i][1] += accelerations[i][1] * dt
    # Update positions
    for i in range(3):
        positions[i][0] += velocities[i][0] * dt
        positions[i][1] += velocities[i][1] * dt
    # Plot
    visualization.plot_positions(positions)

plt.ioff()
plt.show()
