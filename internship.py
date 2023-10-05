import numpy as np
import matplotlib.pyplot as plt

# Define system parameters
m = 1  # Mass (kg)
k = 10  # Spring constant (N/m)
c = 2  # Damping coefficient (Ns/m)
x0 = 0.2  # Initial displacement (m)
v0 = 0  # Initial velocity (m/s)

# Time settings
t_start = 0
t_end = 10
num_points = 1000
t = np.linspace(t_start, t_end, num_points)

# Define the differential equation for the spring-mass-damper system
def spring_mass_damper(x, v, t):
    dxdt = v
    dvdt = -(c/m) * v - (k/m) * x
    return dxdt, dvdt

# Use NumPy to solve the differential equation
x, v = np.zeros_like(t), np.zeros_like(t)
x[0], v[0] = x0, v0

for i in range(1, num_points):
    dxdt, dvdt = spring_mass_damper(x[i-1], v[i-1], t[i-1])
    x[i] = x[i-1] + dxdt * (t[i] - t[i-1])
    v[i] = v[i-1] + dvdt * (t[i] - t[i-1])

# Plot the displacement over time
plt.figure(figsize=(8, 6))
plt.plot(t, x, label='Displacement (m)')
plt.title('Spring-Mass-Damper System Displacement Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Displacement (m)')
plt.grid(True)
plt.legend()
plt.show()
