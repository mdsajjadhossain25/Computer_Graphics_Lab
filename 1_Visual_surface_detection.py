import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np


def drawTriangle(ax):
    """Draw a filled green triangle"""
    x = [10, 50, 100]
    y = [100, 20, 100]

    # Create triangle polygon
    triangle = patches.Polygon([(x[i], y[i]) for i in range(3)],
                               facecolor='green', edgecolor='green', linewidth=2)
    ax.add_patch(triangle)


def drawCircle(ax):
    """Draw a filled blue circle"""
    circle = patches.Circle(
        (100, 100), 45, facecolor='blue', edgecolor='blue', linewidth=2)
    ax.add_patch(circle)


def drawRectangle(ax):
    """Draw a filled red rectangle"""
    rectangle = patches.Rectangle(
        (100, 100), 80, 80, facecolor='red', edgecolor='red', linewidth=2)
    ax.add_patch(rectangle)


def main():
    # Set up the plot to mimic graphics.h behavior
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_facecolor('black')
    ax.invert_yaxis()  # Invert Y-axis to match graphics.h coordinate system

    # Set up the display area
    ax.set_xlim(0, 200)
    ax.set_ylim(0, 200)
    ax.set_aspect('equal')
    ax.set_title('Filled Shapes Drawing', color='white', fontsize=16)
    ax.axis('off')  # Remove axes for cleaner look

    # Drawing sequence (same as C++ code)
    sequence = "RCT"  # Rectangle, Circle, Triangle

    print(f"Drawing shapes in sequence: {sequence}")

    for x in sequence:
        if x == 'C':
            drawCircle(ax)
            print("Drew Circle (Blue)")
        elif x == 'T':
            drawTriangle(ax)
            print("Drew Triangle (Green)")
        else:  # x == 'R'
            drawRectangle(ax)
            print("Drew Rectangle (Red)")

    plt.show()
    print("All shapes drawn successfully!")


if __name__ == "__main__":
    main()

"""
This Python code draws filled shapes (rectangle, circle, triangle) based on a sequence string,
matching the functionality of the original C++ graphics code.

Shape Details:
1. Triangle: Green filled triangle with vertices at (10,100), (50,20), (100,100)
2. Circle: Blue filled circle centered at (100,100) with radius 45
3. Rectangle: Red filled rectangle from (100,100) to (180,180)

The drawing sequence "RCT" means:
- R: Rectangle (Red)
- C: Circle (Blue) 
- T: Triangle (Green)

Key Features:
- Uses matplotlib patches for filled shapes
- Black background to mimic graphics.h appearance
- Inverted Y-axis to match graphics.h coordinate system
- Same colors as C++ code (RED, BLUE, GREEN)
- Same coordinates and dimensions as original

The shapes are drawn with both fill and border in the same color,
equivalent to the setfillstyle(SOLID_FILL) and floodfill() functions in C++.

To run: python3 filled_shapes.py

Try changing the sequence string to draw shapes in different orders!
Examples: "TCR", "CCT", "RRR", etc.
"""
