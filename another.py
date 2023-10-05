import numpy as np
import matplotlib.pyplot as plt

# Define system parameters
m = 1  # Mass (kg)
k = 9  # Spring constant (N/m)

# Time settings
t_start = 0
t_end = 10
num_points = 1000
t = np.linspace(t_start, t_end, num_points)
dt = t[1] - t[0]

# Initial conditions
x0 = 1  # Initial displacement (m)
v0 = 0  # Initial velocity (m/s)

# Initialize arrays to store displacement and velocity
x = np.zeros_like(t)
v = np.zeros_like(t)
x[0] = x0
v[0] = v0

# Numerical solution using the Euler method
for i in range(1, num_points):
    acceleration = -k * x[i-1] / m
    v[i] = v[i-1] + acceleration * dt
    x[i] = x[i-1] + v[i] * dt

# Plot the displacement as a function of time
plt.figure(figsize=(8, 6))
plt.plot(t, x, label='Displacement (m)')
plt.title('Simple Harmonic Oscillator: Displacement Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)
plt.legend()
plt.show()
