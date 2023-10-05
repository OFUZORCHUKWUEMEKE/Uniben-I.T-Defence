
import numpy as np

# Define a square matrix
A = np.array([[1, 2],
              [3, 4]])

# Calculate the inverse of A
A_inv = np.linalg.inv(A)

# Print the original matrix and its inverse
print("Matrix A:")
print(A)
print("Inverse of A:")
print(A_inv)
