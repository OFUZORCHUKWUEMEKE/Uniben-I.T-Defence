import numpy as np
import matplotlib.pyplot as plt

# Define circuit parameters
R = 1000  # Resistance (ohms)
C = 0.001  # Capacitance (farads)
V0 = 10  # Initial voltage (volts)

# Time settings
t_start = 0
t_end = 5
num_points = 1000
t = np.linspace(t_start, t_end, num_points)
dt = t[1] - t[0]

# Initialize arrays for voltage across the capacitor
Vc = np.zeros(num_points)
Vc[0] = V0

# Numerical solution using Euler's method
for i in range(1, num_points):
    Vc[i] = Vc[i-1] + (1 / (R * C)) * (V0 - Vc[i-1]) * dt

# Plot voltage across the capacitor over time
plt.figure(figsize=(8, 6))
plt.plot(t, Vc, label='Voltage across Capacitor (V)')
plt.title('Electric Circuit Analysis: Voltage Across Capacitor Over Time')
plt.xlabel('Time (s)')
plt.ylabel('Voltage (V)')
plt.grid(True)
plt.legend()
plt.show()
