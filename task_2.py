import argparse
import math
import matplotlib.pyplot as plt


def draw_branch(ax, x, y, length, angle, depth, max_depth, ratio, branch_angle, color, lw):
    if depth > max_depth or length <= 0:
        return

    x2 = x + length * math.cos(angle)
    y2 = y + length * math.sin(angle)

    # Draw this segment
    ax.plot([x, x2], [y, y2], color=color, linewidth=lw, solid_capstyle='round')

    # Stop when reached the maximum depth (tips should still be drawn)
    if depth == max_depth:
        return

    next_len = length * ratio
    draw_branch(ax, x2, y2, next_len, angle + branch_angle, depth + 1, max_depth, ratio, branch_angle, color, lw)
    draw_branch(ax, x2, y2, next_len, angle - branch_angle, depth + 1, max_depth, ratio, branch_angle, color, lw)



def pythagoras_tree(level=8, size=1.0):
    fig, ax = plt.subplots(figsize=(8, 8))

    # Visual parameters tuned to the provided example
    color = "#a33"  # reddish brown
    lw = 1.5
    ratio = 0.75
    branch_angle = math.pi / 6  # 30 degrees

    # Start from the ground with a vertical trunk pointing upward
    draw_branch(ax, 0.0, 0.0, size, math.pi / 2, 0, level, ratio, branch_angle, color, lw)

    ax.set_aspect('equal')
    ax.axis('off')
    ax.set_xlim(-size * 2.2, size * 2.2)
    ax.set_ylim(0, size * 3.0)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fractal tree visualization")
    parser.add_argument("-n", "--level", type=int, default=8, help="Recursion level")
    parser.add_argument("--size", type=float, default=1.0, help="Base branch length")
    args = parser.parse_args()
    pythagoras_tree(args.level, args.size)
