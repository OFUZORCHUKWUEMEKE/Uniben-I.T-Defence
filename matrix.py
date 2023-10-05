import numpy as np

def print_menu():
    print("\nMatrix Calculator Menu:")
    print("1. Add Matrices")
    print("2. Subtract Matrices")
    print("3. Multiply Matrices")
    print("4. Calculate Determinant")
    print("5. Calculate Inverse")
    print("6. Transpose Matrix")
    print("7. Exit")

def get_matrix_input(prompt="Enter the matrix (e.g., 1 2; 3 4): "):
    matrix_str = input(prompt)
    matrix = np.array([list(map(float, row.split())) for row in matrix_str.split(';')])
    return matrix

def add_matrices():
    matrix1 = get_matrix_input("Enter the first matrix: ")
    matrix2 = get_matrix_input("Enter the second matrix: ")
    result = matrix1 + matrix2
    print("Result:")
    print(result)

def subtract_matrices():
    matrix1 = get_matrix_input("Enter the first matrix: ")
    matrix2 = get_matrix_input("Enter the second matrix: ")
    result = matrix1 - matrix2
    print("Result:")
    print(result)

def multiply_matrices():
    matrix1 = get_matrix_input("Enter the first matrix: ")
    matrix2 = get_matrix_input("Enter the second matrix: ")
    result = np.dot(matrix1, matrix2)
    print("Result:")
    print(result)

def calculate_determinant():
    matrix = get_matrix_input("Enter the matrix: ")
    det = np.linalg.det(matrix)
    print("Determinant:")
    print(det)

def calculate_inverse():
    matrix = get_matrix_input("Enter the matrix: ")
    try:
        inv_matrix = np.linalg.inv(matrix)
        print("Inverse Matrix:")
        print(inv_matrix)
    except np.linalg.LinAlgError:
        print("Inverse does not exist for this matrix.")

def transpose_matrix():
    matrix = get_matrix_input("Enter the matrix: ")
    transposed_matrix = np.transpose(matrix)
    print("Transposed Matrix:")
    print(transposed_matrix)

def main():
    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            add_matrices()
        elif choice == '2':
            subtract_matrices()
        elif choice == '3':
            multiply_matrices()
        elif choice == '4':
            calculate_determinant()
        elif choice == '5':
            calculate_inverse()
        elif choice == '6':
            transpose_matrix()
        elif choice == '7':
            print("Exiting the matrix calculator.")
            break
        else:
            print("Invalid choice. Please select a valid option (1-7).")

if __name__ == "__main__":
    main()
