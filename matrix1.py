import numpy as np

# Define two matrices
A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

# Calculate the product of A and B
result = np.dot(A, B)

# Print the result
print("Matrix A:")
print(A)
print("Matrix B:")
print(B)
print("Matrix A * B:")
print(result)
