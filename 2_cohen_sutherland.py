import matplotlib.pyplot as plt

# Clipping window boundaries
x_left, x_right, y_bottom, y_top = 120, 500, 100, 350

# Region codes
LEFT, RIGHT, BOTTOM, TOP = 1, 2, 4, 8

def region_code(x, y):
    code = 0
    if x > x_right:
        code |= RIGHT
    elif x < x_left:
        code |= LEFT
    if y > y_top:
        code |= TOP
    elif y < y_bottom:
        code |= BOTTOM
    return code

def cohen_sutherland(x1, y1, x2, y2, ax):
    code1 = region_code(x1, y1)
    code2 = region_code(x2, y2)

    while True:
        if not (code1 | code2):
            # Line is completely inside → draw clipped line
            ax.plot([x1, x2], [y1, y2], color="white", linewidth=2)
            return
        elif code1 & code2:
            # Completely outside
            return
        else:
            x, y = 0, 0
            out_code = code1 if code1 else code2

            if out_code & TOP:
                y = y_top
                x = x1 + (x2 - x1) / (y2 - y1) * (y - y1)
            elif out_code & BOTTOM:
                y = y_bottom
                x = x1 + (x2 - x1) / (y2 - y1) * (y - y1)
            elif out_code & LEFT:
                x = x_left
                y = y1 + (y2 - y1) / (x2 - x1) * (x - x1)
            elif out_code & RIGHT:
                x = x_right
                y = y1 + (y2 - y1) / (x2 - x1) * (x - x1)

            if out_code == code1:
                x1, y1 = x, y
                code1 = region_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = region_code(x2, y2)

def main():
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.set_facecolor("black")

    # Draw clipping window (yellow rectangle)
    rect_x = [x_left, x_right, x_right, x_left, x_left]
    rect_y = [y_bottom, y_bottom, y_top, y_top, y_bottom]
    ax.plot(rect_x, rect_y, color="yellow")

    # Original line (red)
    x1, y1, x2, y2 = 50, 200, 500, 400
    ax.plot([x1, x2], [y1, y2], color="red", linestyle="--")

    # Clipped line (white)
    cohen_sutherland(x1, y1, x2, y2, ax)

    ax.set_xlim(0, 600)
    ax.set_ylim(0, 500)
    ax.set_aspect("equal")
    plt.show()

if __name__ == "__main__":
    main()
