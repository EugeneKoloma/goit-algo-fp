import argparse
import math
import matplotlib.pyplot as plt


def draw_square(ax, x, y, size, angle, color):
    c = math.cos(angle)
    s = math.sin(angle)
    vx = (c * size, s * size)
    vy = (-s * size, c * size)
    p0 = (x, y)
    p1 = (x + vx[0], y + vx[1])
    p2 = (p1[0] + vy[0], p1[1] + vy[1])
    p3 = (x + vy[0], y + vy[1])
    ax.fill([p0[0], p1[0], p2[0], p3[0]], [p0[1], p1[1], p2[1], p3[1]], color=color, ec=color)
    return p3, p2


def draw_tree(ax, x, y, size, angle, depth, max_depth):
    if depth > max_depth:
        return
    t = depth / (max_depth + 1)
    color = f"#{int(30 + 80*t):02x}{int(80 + 120*t):02x}{int(30 + 80*t):02x}"
    left_top, right_top = draw_square(ax, x, y, size, angle, color)
    lx, ly = left_top
    rx, ry = right_top
    next_size = size / math.sqrt(2)
    draw_tree(ax, lx, ly, next_size, angle + math.pi / 4, depth + 1, max_depth)
    draw_tree(ax, rx, ry, next_size, angle - math.pi / 4, depth + 1, max_depth)


def pythagoras_tree(level=8, size=1.0):
    fig, ax = plt.subplots(figsize=(8, 8))
    draw_tree(ax, 0.0, 0.0, size, 0.0, 0, level)
    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-size*2, size*2)
    ax.set_ylim(0, size*3)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Pythagoras tree visualization")
    parser.add_argument("-n", "--level", type=int, default=8, help="Recursion level")
    parser.add_argument("--size", type=float, default=1.0, help="Base square size")
    args = parser.parse_args()
    pythagoras_tree(args.level, args.size)
