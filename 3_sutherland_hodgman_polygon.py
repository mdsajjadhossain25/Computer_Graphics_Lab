import matplotlib.pyplot as plt

# Clipping window boundaries
x_min, y_min = 120, 100
x_max, y_max = 500, 350


def inside(p, edge):
    x, y = p
    if edge == "LEFT":
        return x >= x_min
    if edge == "RIGHT":
        return x <= x_max
    if edge == "BOTTOM":
        return y >= y_min
    if edge == "TOP":
        return y <= y_max


def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:
        m = None
    else:
        m = (y2 - y1) / (x2 - x1)

    if edge == "LEFT":
        x, y = x_min, y1 + (x_min - x1) * m
    elif edge == "RIGHT":
        x, y = x_max, y1 + (x_max - x1) * m
    elif edge == "BOTTOM":
        if m is None:
            x, y = x1, y_min
        else:
            x, y = x1 + (y_min - y1) / m, y_min
    elif edge == "TOP":
        if m is None:
            x, y = x1, y_max
        else:
            x, y = x1 + (y_max - y1) / m, y_max
    return (x, y)


def clip_polygon(polygon, edge):
    clipped = []
    n = len(polygon)
    for i in range(n):
        curr = polygon[i]
        prev = polygon[i-1]
        if inside(curr, edge):
            if inside(prev, edge):
                clipped.append(curr)
            else:
                clipped.append(intersect(prev, curr, edge))
                clipped.append(curr)
        else:
            if inside(prev, edge):
                clipped.append(intersect(prev, curr, edge))
    return clipped


def sutherland_hodgman(polygon):
    for edge in ["LEFT", "RIGHT", "BOTTOM", "TOP"]:
        polygon = clip_polygon(polygon, edge)
    return polygon


def main():
    # Example polygon
    polygon = [(100, 150), (200, 50), (300, 100),
               (350, 300), (250, 350), (150, 300)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Set white backgrounds
    ax1.set_facecolor("white")
    ax2.set_facecolor("white")

    # Draw original polygon
    xs, ys = zip(*polygon)
    ax1.fill(xs, ys, facecolor="lightcoral", alpha=0.7,
             edgecolor="darkred", linewidth=2)
    rect_x = [x_min, x_max, x_max, x_min, x_min]
    rect_y = [y_min, y_min, y_max, y_max, y_min]
    ax1.plot(rect_x, rect_y, color="blue", linewidth=2)
    ax1.set_title("Original Polygon", color="black", fontsize=14)
    ax1.set_xlim(50, 600)
    ax1.set_ylim(50, 400)
    ax1.set_aspect("equal")
    ax1.grid(True, alpha=0.3)

    # Clip polygon
    clipped = sutherland_hodgman(polygon)
    if clipped:
        xs, ys = zip(*clipped)
        ax2.fill(xs, ys, facecolor="lightgreen", alpha=0.7,
                 edgecolor="darkgreen", linewidth=2)
    ax2.plot(rect_x, rect_y, color="blue", linewidth=2)
    ax2.set_title("Clipped Polygon", color="black", fontsize=14)
    ax2.set_xlim(50, 600)
    ax2.set_ylim(50, 400)
    ax2.set_aspect("equal")
    ax2.grid(True, alpha=0.3)

    plt.suptitle("Sutherland-Hodgman Polygon Clipping Algorithm",
                 fontsize=16, color="black")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
