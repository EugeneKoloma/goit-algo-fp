import argparse
import random
import matplotlib.pyplot as plt

ANALYTICAL = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}


def simulate(n_rolls=100_000):
    counts = {s: 0 for s in range(2, 13)}
    for _ in range(n_rolls):
        s = random.randint(1, 6) + random.randint(1, 6)
        counts[s] += 1
    probs = {s: counts[s]/n_rolls for s in counts}
    return counts, probs


def plot_probs(probs):
    xs = list(range(2, 13))
    ys = [probs[s] for s in xs]
    ya = [ANALYTICAL[s] for s in xs]
    plt.figure(figsize=(8, 5))
    plt.bar(xs, ys, color="#1296F0", alpha=0.7, label="Monte Carlo")
    plt.plot(xs, ya, color="#e74c3c", marker="o", label="Analytical")
    plt.xticks(xs)
    plt.ylabel("Probability")
    plt.xlabel("Sum of two dice")
    plt.title("Two dice sum probabilities")
    plt.legend()
    plt.tight_layout()
    plt.show()


def compare(probs):
    print("Sum  MC(%)  Analytic(%)  Abs diff(%)")
    for s in range(2, 13):
        mc = probs[s] * 100
        an = ANALYTICAL[s] * 100
        print(f"{s:>3}  {mc:5.2f}     {an:5.2f}       {abs(mc-an):5.2f}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Monte Carlo simulation for two dice")
    parser.add_argument("-n", "--rolls", type=int, default=100000, help="Number of rolls")
    args = parser.parse_args()

    counts, probs = simulate(args.rolls)
    compare(probs)
    plot_probs(probs)
