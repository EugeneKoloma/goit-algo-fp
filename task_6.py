import argparse

items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}


def greedy_algorithm(items_dict, budget):
    goods = [
        (name, v["cost"], v["calories"], v["calories"] / v["cost"]) for name, v in items_dict.items()
    ]
    goods.sort(key=lambda x: x[3], reverse=True)
    picked = []
    spent = 0
    calories = 0
    for name, cost, cal, ratio in goods:
        if spent + cost <= budget:
            picked.append(name)
            spent += cost
            calories += cal
    return picked, spent, calories


def dynamic_programming(items_dict, budget):
    names = list(items_dict.keys())
    costs = [items_dict[n]["cost"] for n in names]
    cals = [items_dict[n]["calories"] for n in names]
    n = len(names)

    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    take = [[False] * (budget + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        cost_i = costs[i - 1]
        cal_i = cals[i - 1]
        for b in range(budget + 1):
            dp[i][b] = dp[i - 1][b]
            if cost_i <= b and dp[i - 1][b - cost_i] + cal_i > dp[i][b]:
                dp[i][b] = dp[i - 1][b - cost_i] + cal_i
                take[i][b] = True

    b = budget
    picked = []
    for i in range(n, 0, -1):
        if take[i][b]:
            picked.append(names[i - 1])
            b -= costs[i - 1]
    picked.reverse()
    total_cost = sum(items_dict[n]["cost"] for n in picked)
    total_cal = sum(items_dict[n]["calories"] for n in picked)
    return picked, total_cost, total_cal


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Food selection by greedy and DP")
    parser.add_argument("budget", type=int, nargs="?", default=100, help="Budget")
    args = parser.parse_args()

    g_items, g_cost, g_cal = greedy_algorithm(items, args.budget)
    print("Greedy:", g_items, "+cost=", g_cost, "+cal=", g_cal)

    d_items, d_cost, d_cal = dynamic_programming(items, args.budget)
    print("DP:", d_items, "+cost=", d_cost, "+cal=", d_cal)
