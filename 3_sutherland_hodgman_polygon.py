import matplotlib.pyplot as plt

# Clipping window boundaries
x_min, y_min = 120, 100
x_max, y_max = 500, 350

def inside(p, edge):
    x, y = p
    if edge == "LEFT":   return x >= x_min
    if edge == "RIGHT":  return x <= x_max
    if edge == "BOTTOM": return y >= y_min
    if edge == "TOP":    return y <= y_max

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
        if m is None: x, y = x1, y_min
        else: x, y = x1 + (y_min - y1) / m, y_min
    elif edge == "TOP":
        if m is None: x, y = x1, y_max
        else: x, y = x1 + (y_max - y1) / m, y_max
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
    polygon = [(100, 150), (200, 50), (300, 100), (350, 300), (250, 350), (150, 300)]

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

    # Draw original polygon
    xs, ys = zip(*polygon)
    ax1.fill(xs, ys, facecolor="red", alpha=0.5, edgecolor="black")
    rect_x = [x_min, x_max, x_max, x_min, x_min]
    rect_y = [y_min, y_min, y_max, y_max, y_min]
    ax1.plot(rect_x, rect_y, color="blue")
    ax1.set_title("Original Polygon")
    ax1.set_xlim(50, 600); ax1.set_ylim(50, 400); ax1.set_aspect("equal")

    # Clip polygon
    clipped = sutherland_hodgman(polygon)
    if clipped:
        xs, ys = zip(*clipped)
        ax2.fill(xs, ys, facecolor="green", alpha=0.5, edgecolor="black")
    ax2.plot(rect_x, rect_y, color="blue")
    ax2.set_title("Clipped Polygon")
    ax2.set_xlim(50, 600); ax2.set_ylim(50, 400); ax2.set_aspect("equal")

    plt.show()

if __name__ == "__main__":
    main()
