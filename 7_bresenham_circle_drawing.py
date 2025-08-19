import matplotlib.pyplot as plt
import numpy as np


def drawCircle(xc, yc, radius):
    """Draw circle using Bresenham's Circle Drawing Algorithm (Midpoint Circle Algorithm)"""
    x = 0
    y = radius
    p = 1 - radius  # Initial decision parameter

    # Store all pixels to draw
    circle_pixels = []

    # Plot initial points in all 8 octants
    def plot8Points(xc, yc, x, y):
        points = [
            (xc + x, yc + y),  # Octant 1
            (xc - x, yc + y),  # Octant 2
            (xc + x, yc - y),  # Octant 3
            (xc - x, yc - y),  # Octant 4
            (xc + y, yc + x),  # Octant 5
            (xc - y, yc + x),  # Octant 6
            (xc + y, yc - x),  # Octant 7
            (xc - y, yc - x)   # Octant 8
        ]
        return points

    # Add initial points
    circle_pixels.extend(plot8Points(xc, yc, x, y))

    # Bresenham's circle algorithm
    while x < y:
        x += 1

        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1

        # Add points in all 8 octants
        circle_pixels.extend(plot8Points(xc, yc, x, y))

    return circle_pixels


def main():
    # Set up the plot to mimic graphics.h behavior
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.set_facecolor('black')
    ax.invert_yaxis()  # Invert Y-axis to match graphics.h coordinate system

    # Define circle parameters
    xc, yc = 250, 250  # Center coordinates
    radius = 100       # Radius

    # Draw circle using Bresenham's algorithm
    circle_pixels = drawCircle(xc, yc, radius)

    # Remove duplicate pixels (since some octants may overlap)
    circle_pixels = list(set(circle_pixels))

    # Extract x and y coordinates
    x_coords = [pixel[0] for pixel in circle_pixels]
    y_coords = [pixel[1] for pixel in circle_pixels]

    # Plot the circle as individual pixels (points)
    ax.scatter(x_coords, y_coords, c='white', s=2, marker='s')

    # Mark the center point
    ax.scatter([xc], [yc], c='red', s=50, marker='+',
               linewidth=3, label='Center')

    # Set up the display
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 500)
    ax.set_aspect('equal')
    ax.set_title(
        f'Bresenham\'s Circle Drawing Algorithm\nCenter: ({xc}, {yc}), Radius: {radius}', color='white')
    ax.grid(True, alpha=0.3)
    ax.legend()

    plt.tight_layout()
    plt.show()

    # Print the algorithm details for educational purposes
    print(f"Circle with center ({xc}, {yc}) and radius {radius}")
    print(f"Total pixels drawn: {len(circle_pixels)}")
    print(f"Algorithm uses 8-way symmetry to draw complete circle")
    print(f"Decision parameter p determines whether to move diagonally or horizontally")


if __name__ == "__main__":
    main()

"""
This Python code implements Bresenham's Circle Drawing Algorithm (also known as Midpoint Circle Algorithm),
which is used to draw circles in computer graphics by determining which pixels should be selected 
to form a close approximation to a circle.

The algorithm works by:
1. Starting from (0, radius) and using 8-way symmetry
2. Using a decision parameter p to determine the next pixel
3. Drawing pixels in all 8 octants simultaneously
4. Using only integer arithmetic for efficiency

Key features:
- Uses integer arithmetic only (no floating-point calculations)
- Efficient due to 8-way symmetry (only calculates 1/8 of circle)
- Produces smooth circular curves
- Based on the midpoint criterion

Algorithm steps:
- Initial: x = 0, y = radius, p = 1 - radius
- For each step: increment x, update p and possibly decrement y
- Plot 8 symmetric points for each (x, y) pair

Sample output:
- Draws a circle with center (250, 250) and radius 100
- Shows individual pixels as white squares on black background
- Red '+' marker at the center for reference
- Grid overlay for better visualization

To run: python3 bresenham_circle_drawing.py

The circle algorithm is fundamental in computer graphics and is used because it produces
smooth circles using only integer arithmetic, making it very fast for real-time applications.
"""
