import matplotlib.pyplot as plt
import numpy as np


def drawLine(x1, y1, x2, y2, pixels):
    """Draw line using Bresenham's line drawing algorithm"""
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

    dx = x2 - x1
    dy = abs(y1 - y2)
    p = 2 * dy - dx

    x, y = x1, y1

    # Store all pixels to draw
    line_pixels = []

    for x in range(x1, x2 + 1):
        line_pixels.append((x, y))

        if p >= 0:
            p += 2 * (dy - dx)
            if y1 < y2:
                y += 1
            else:
                y -= 1
        else:
            p += 2 * dy

    return line_pixels


def main():
    # Set up the plot to mimic graphics.h behavior
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.set_facecolor('black')
    ax.invert_yaxis()  # Invert Y-axis to match graphics.h coordinate system

    # Define line endpoints (same as C++ code)
    x1, y1 = 100, 100
    x2, y2 = 400, 370

    # Create pixel grid for visualization
    pixels = np.zeros((500, 500))  # Create a 500x500 grid

    # Draw line using Bresenham's algorithm
    line_pixels = drawLine(x1, y1, x2, y2, pixels)

    # Extract x and y coordinates
    x_coords = [pixel[0] for pixel in line_pixels]
    y_coords = [pixel[1] for pixel in line_pixels]

    # Plot the line as individual pixels (points)
    ax.scatter(x_coords, y_coords, c='white', s=1, marker='s')

    # Set up the display
    ax.set_xlim(0, 500)
    ax.set_ylim(0, 500)
    ax.set_aspect('equal')
    ax.set_title('Bresenham\'s Line Drawing Algorithm', color='white')
    ax.grid(True, alpha=0.3)

    # Add endpoint markers for reference
    ax.scatter([x1, x2], [y1, y2], c='red', s=50,
               marker='o', label='Endpoints')
    ax.legend()

    plt.tight_layout()
    plt.show()

    # Print the algorithm steps for educational purposes
    print(f"Line from ({x1}, {y1}) to ({x2}, {y2})")
    print(f"dx = {x2 - x1}, dy = {abs(y1 - y2)}")
    print(f"Total pixels drawn: {len(line_pixels)}")


if __name__ == "__main__":
    main()

"""
This Python code implements Bresenham's Line Drawing Algorithm, which is used to draw lines
in computer graphics by determining which pixels should be selected to form a close 
approximation to a straight line between two points.

The algorithm works by:
1. Calculating dx (horizontal distance) and dy (vertical distance)
2. Using a decision parameter p to determine when to increment the y-coordinate
3. Drawing pixels step by step from start to end point

Key features:
- Uses integer arithmetic only (no floating-point calculations)
- Efficient and fast
- Produces smooth lines with minimal gaps

Sample output:
- Draws a line from (100, 100) to (400, 370)
- Shows individual pixels as white squares on black background
- Displays endpoints in red for reference
- Prints algorithm statistics

To run: python3 bresenham_line_drawing.py
"""
