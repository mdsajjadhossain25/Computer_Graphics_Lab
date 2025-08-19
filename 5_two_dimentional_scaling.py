import sys
import matplotlib.pyplot as plt


def draw(x, y):
    """Draw polygon by connecting vertices"""
    n = len(x)
    xs = x + [x[0]]  # Close the polygon
    ys = y + [y[0]]
    plt.plot(xs, ys, linewidth=2)


def scale(x, y, n, sfx, sfy):
    """Apply 2D scaling to polygon vertices"""
    for i in range(n):
        x[i] = x[i] * sfx
        y[i] = y[i] * sfy


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

    sfx, sfy = map(int, input().split())  # Scaling factors

    # Setup matplotlib to mimic graphics.h behavior
    plt.figure(figsize=(10, 8))
    plt.gca().set_facecolor('black')
    plt.gca().invert_yaxis()  # Invert Y-axis to match graphics.h coordinate system

    # Draw white polygon before scaling
    plt.plot([], [], color='white', label='Before Scaling', linewidth=2)
    draw(x.copy(), y.copy())
    plt.gca().lines[-1].set_color('white')

    # Apply 2d geometric scaling
    scale(x, y, n, sfx, sfy)

    # Draw yellow polygon after scaling
    draw(x, y)
    plt.gca().lines[-1].set_color('yellow')

    plt.axis('equal')
    plt.legend()
    plt.title('2D Polygon Scaling')
    plt.show()


if __name__ == "__main__":
    main()

"""
Sample Input (enter each line separately when running):
4
100 100
100 150
150 150
150 100
2 2

Alternative: You can also create an input file (input.txt) with:
4
100 100
100 150
150 150
150 100
2 2

Then run: python3 5_two_dimentional_scaling.py < input.txt

The input format is:
- First line: number of vertices (n)
- Next n lines: x y coordinates of each vertex
- Last line: scaling factors (sfx sfy)

This will create a rectangle with vertices at (100,100), (100,150), (150,150), (150,100)
and scale it by factors 2 and 2 (doubling both x and y coordinates).
The original polygon will be shown in white and the scaled polygon in yellow.
"""
