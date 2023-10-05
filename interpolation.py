import numpy as np

def linear_interpolation(x_known, y_known, x_interpolate):
    # Check if the input lists have the same length
    if len(x_known) != len(y_known):
        raise ValueError("Input lists must have the same length.")
    
    # Find the two known points surrounding the interpolation point
    for i in range(len(x_known) - 1):
        if x_known[i] <= x_interpolate <= x_known[i+1]:
            x0, x1 = x_known[i], x_known[i+1]
            y0, y1 = y_known[i], y_known[i+1]
            break
    else:
        raise ValueError("Interpolation point is outside the range of known data.")
    
    # Perform linear interpolation
    interpolated_value = y0 + (x_interpolate - x0) * (y1 - y0) / (x1 - x0)
    return interpolated_value

def main():
    # Known data points
    x_known = [1, 2, 3, 4, 5]
    y_known = [10, 15, 24, 38, 55]
    
    # Interpolation point
    x_interpolate = float(input("Enter the interpolation point: "))
    
    try:
        result = linear_interpolation(x_known, y_known, x_interpolate)
        print(f"Interpolated value at {x_interpolate} is approximately {result:.2f}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
