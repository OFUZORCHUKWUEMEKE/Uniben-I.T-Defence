import numpy as np
from scipy.optimize import minimize

# Define design requirements
k_desired = 1000  # Desired spring constant (N/m)
L0 = 0.1  # Free length (m)
F_max = 500  # Maximum load (N)

# Material properties
E = 200e9  # Young's modulus (Pa)
sigma_allow = 250e6  # Allowable stress (Pa)

# Objective function to minimize spring mass
def objective(x):
    d, N = x  # Wire diameter (m), Number of coils
    # Calculate spring constant using spring design equations
    k_actual = (G * d**4) / (8 * D**3 * N)
    # Calculate spring mass
    mass = np.pi * d**2 * L0 * rho * N
    # Define an objective to minimize mass while meeting the desired spring constant
    return mass

# Constraints function to ensure desired spring constant and allowable stress
def constraints(x):
    d, N = x  # Wire diameter (m), Number of coils
    # Calculate spring constant using spring design equations
    k_actual = (G * d**4) / (8 * D**3 * N)
    # Calculate stress in the spring wire
    stress = (F_max / A) + ((k_actual - k_desired) * L0)
    # Constraints: Spring constant must match, and stress must be below allowable
    return [k_desired - k_actual, sigma_allow - stress]

# Material properties for steel wire
rho = 7850  # Density (kg/m^3)
G = 77e9  # Shear modulus (Pa)
D = 2 * L0  # Mean coil diameter (m)
A = np.pi * (d**2) / 4  # Cross-sectional area (m^2)

# Initial guess for wire diameter and number of coils
x0 = np.array([0.01, 10])

# Perform optimization to find wire diameter and number of coils
result = minimize(objective, x0, constraints=constraints, method='SLSQP')

# Extract the optimized values
optimal_diameter, optimal_coils = result.x

# Print the optimized values
print("Optimized Wire Diameter:", optimal_diameter, "m")
print("Optimized Number of Coils:", optimal_coils)

