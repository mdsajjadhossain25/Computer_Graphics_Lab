import sys
import math
import matplotlib.pyplot as plt


def draw(x, y):
    """Draw polygon by connecting vertices"""
    n = len(x)
    xs = x + [x[0]]  # Close the polygon
    ys = y + [y[0]]
    plt.plot(xs, ys, linewidth=2)


def rotation(x, y, n, angle, xp, yp):
    """Apply 2D rotation to polygon vertices"""
    for i in range(n):
        radian = angle * (math.pi / 180)
        sin_term = math.sin(radian)
        cos_term = math.cos(radian)
        x_shift = x[i] - xp
        y_shift = y[i] - yp
        x[i] = xp + (x_shift * cos_term) - (y_shift * sin_term)
        y[i] = yp + (x_shift * sin_term) + (y_shift * cos_term)


def main():
    # Read input
    n = int(input())  # Total vertex of the polygon
    x = []
    y = []

    # Read (x,y) coordinates of vertex points
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)

    angle = int(input())  # Rotation angle in degree
    x_pivot, y_pivot = map(int, input().split())  # Pivot point coordinates

    # Setup matplotlib to mimic graphics.h behavior
    plt.figure(figsize=(10, 8))
    plt.gca().set_facecolor('white')
    plt.gca().invert_yaxis()  # Invert Y-axis to match graphics.h coordinate system

    # Draw black polygon before rotation
    plt.plot([], [], color='black', label='Before Rotation', linewidth=2)
    draw(x.copy(), y.copy())
    plt.gca().lines[-1].set_color('black')

    # Apply 2d geometric rotation
    rotation(x, y, n, angle, x_pivot, y_pivot)

    # Draw red polygon after rotation
    draw(x, y)
    plt.gca().lines[-1].set_color('red')

    plt.axis('equal')
    plt.legend()
    plt.title('2D Polygon Rotation', color='black')
    plt.show()


if __name__ == "__main__":
    main()

"""
Sample Input (enter each line separately when running):
4
100 100
100 200
200 200
200 100
45
200 200

Alternative: You can also create an input file (input.txt) with:
4
100 100
100 200
200 200
200 100
45
200 200

Then run: python3 rotation_standalone.py < input.txt

The input format is:
- First line: number of vertices (n)
- Next n lines: x y coordinates of each vertex
- Next line: rotation angle in degrees
- Last line: pivot point coordinates (xp yp)

This will create a square with vertices at (100,100), (100,200), (200,200), (200,100)
and rotate it 45 degrees around pivot point (200,200).
The original polygon will be shown in black and the rotated polygon in red.
"""
