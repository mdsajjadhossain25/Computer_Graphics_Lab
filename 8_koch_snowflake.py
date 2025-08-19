# Koch Snowflake (fractal) — outline or filled
import numpy as np
import matplotlib.pyplot as plt

def koch_curve(p1: complex, p2: complex, order: int):
    """Return list of complex points for a Koch curve segment p1→p2."""
    if order == 0:
        return [p1, p2]
    a = p1 + (p2 - p1) / 3
    b = p1 + 2 * (p2 - p1) / 3
    # rotate (b-a) by +60° to get the peak
    peak = a + (b - a) * np.exp(1j * np.pi / 3)
    return (
        koch_curve(p1, a, order - 1)[:-1] +
        koch_curve(a, peak, order - 1)[:-1] +
        koch_curve(peak, b, order - 1)[:-1] +
        koch_curve(b, p2, order - 1)
    )

def koch_snowflake(order=5, scale=1.0):
    """Return x,y arrays for a Koch snowflake of a given order."""
    # Equilateral triangle (centered nicely)
    p1 = scale * np.exp(1j * np.deg2rad(90))   # top
    p2 = scale * np.exp(1j * np.deg2rad(210))  # bottom-left
    p3 = scale * np.exp(1j * np.deg2rad(330))  # bottom-right

    side1 = koch_curve(p1, p2, order)[:-1]
    side2 = koch_curve(p2, p3, order)[:-1]
    side3 = koch_curve(p3, p1, order)
    pts = np.array(side1 + side2 + side3)
    return pts.real, pts.imag

if __name__ == "__main__":
    ORDER = 5          # try 3–6
    SCALE = 1.0
    FILL  = False      # set True to fill the snowflake

    x, y = koch_snowflake(order=ORDER, scale=SCALE)

    plt.figure(figsize=(7, 7))
    if FILL:
        plt.fill(x, y)
    else:
        plt.plot(x, y, linewidth=1)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()
