import sys
import matplotlib.pyplot as plt


def draw(x, y):
    """Draw polygon by connecting vertices"""
    n = len(x)
    xs = x + [x[0]]  # Close the polygon
    ys = y + [y[0]]
    plt.plot(xs, ys, linewidth=2)


def translate(x, y, tx, ty):
    """Apply 2D translation to polygon vertices"""
    n = len(x)
    for i in range(n):
        x[i] += tx
        y[i] += ty


def main():
    # Read input
    n = int(input())  # Number of vertex of the polygon
    x = []
    y = []

    # Read (x,y) coordinates of vertex points
    for i in range(n):
        xi, yi = map(int, input().split())
        x.append(xi)
        y.append(yi)

    tx, ty = map(int, input().split())  # Translation factors

    # Setup matplotlib to mimic graphics.h behavior
    plt.figure(figsize=(10, 8))
    plt.gca().set_facecolor('white')
    plt.gca().invert_yaxis()  # Invert Y-axis to match graphics.h coordinate system

    # Draw black polygon before translation
    plt.plot([], [], color='black', label='Before Translation', linewidth=2)
    draw(x.copy(), y.copy())
    plt.gca().lines[-1].set_color('black')

    # Apply 2d geometric translation
    translate(x, y, tx, ty)

    # Draw red polygon after translation
    draw(x, y)
    plt.gca().lines[-1].set_color('red')

    plt.axis('equal')
    plt.legend()
    plt.title('2D Polygon Translation', color='black')
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
150 150

Alternative: You can also create an input file (input.txt) with:
4
100 100
100 200
200 200
200 100
150 150

Then run: python3 5_two_dimentional_translation.py < input.txt

The input format is:
- First line: number of vertices (n)
- Next n lines: x y coordinates of each vertex
- Last line: translation factors (tx ty)

This will create a square with vertices at (100,100), (100,200), (200,200), (200,100)
and translate it by 150 units in both x and y directions.
The original polygon will be shown in black and the translated polygon in red.
"""
