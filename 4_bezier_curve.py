import math
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def factorial(n: int) -> int:
    if n:
        return n * factorial(n - 1)
    return 1


def nCr(n: int, r: int) -> float:
    return factorial(n) / float(factorial(r) * factorial(n - r))


def bezier_function(k: int, n: int, u: float) -> float:
    return nCr(n, k) * pow(u, k) * pow(1 - u, n - k)


def bezier_curve(points, eps: float = 1e-4):
    n = len(points) - 1
    xs, ys = [], []
    steps = int(1.0 / eps)

    for i in range(steps + 1):
        u = i * eps
        x = 0.0
        y = 0.0
        for k in range(n + 1):
            bez = bezier_function(k, n, u)
            x += points[k][0] * bez
            y += points[k][1] * bez
        xs.append(x)
        ys.append(y)

    # Prepare canvas
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")

    # Draw curve as black pixels (points)
    ax.plot(xs, ys, linestyle="None", marker=".", markersize=2, color="black")

    # Draw control points and small circles (radius ≈ 5 pixels)
    for (cx, cy) in points:
        ax.plot(cx, cy, marker=".", color="red",
                markersize=8)  # control points in red
        circ = Circle((cx, cy), radius=5, edgecolor="black",
                      facecolor="none", linewidth=1)
        ax.add_patch(circ)

    # Viewport similar to pixel coordinates, invert Y to match graphics.h screen coords
    pad = 20
    max_x = max(p[0] for p in points) + pad
    max_y = max(p[1] for p in points) + pad
    ax.set_xlim(0, max_x)
    ax.set_ylim(max_y, 0)  # invert Y
    ax.set_aspect("equal")
    ax.axis("off")

    plt.show()


def main():
    points = [(27, 243), (101, 47), (324, 197), (437, 23)]
    bezier_curve(points)


if __name__ == "__main__":
    main()
